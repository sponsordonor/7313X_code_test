import datetime
import inspect

from django import db
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

import django.contrib.postgres.fields as postgres

DO_NOTHING = db.models.DO_NOTHING
CASCADE = db.models.CASCADE

class ChoiceEnum(object):
    @classmethod
    def choices(cls):
        attrs = inspect.getmembers(
            cls,
            lambda m: not inspect.isroutine(m))
        attrs = [a for a in attrs if
                 not (a[0].startswith('__') or
                      a[0].endswith('__'))]
        return [(a[1], a[0]) for a in attrs]


class User(AbstractUser):
    donor=models.OneToOneField("Donor", on_delete=CASCADE, null=True, blank=True)
    sponsor=models.OneToOneField("Sponsor", on_delete=CASCADE, null=True, blank=True)

class Donor(models.Model):
    pass

class Sponsor(models.Model):

    @property
    def match(self):
        qs = self.matches.filter(state=Match.State.active)
        if qs.exists():
            return qs[0]
        return None

class Donation(models.Model):
    class State(ChoiceEnum):
        process='Processing'
        paid='Paid'
        initiated='Initiated'

    state = models.CharField(choices=State.choices(), max_length=20)
    title = models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    donor=models.ForeignKey("Donor", on_delete=CASCADE)
    amount=models.DecimalField(decimal_places=2, max_digits=9)
    campaign=models.ForeignKey("Campaign", on_delete=CASCADE)
    created_date=models.DateTimeField(default=timezone.now)

    def is_valid_match(self, match):
        return match.max_amount >= self.amount

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            for match in Match.objects.filter(state=Match.State.active):
                if self.is_valid_match(match):
                    donation_match = DonationMatch(
                        self,
                        match
                    )
                    donation_match.save()
                #TODO: campaigns

class DonationMatch(models.Model):
    donation = models.ForeignKey('Donation', on_delete=CASCADE)
    match = models.ForeignKey('Match', on_delete=CASCADE)

class Match(models.Model):
    class State(ChoiceEnum):
        active='Active'
        inactive='Inactive'
        completed='Completed'

    sponsor = models.ForeignKey('Sponsor', on_delete=CASCADE, related_name='matches')
    amount = models.IntegerField(default=0)
    max_amount = models.IntegerField(default=0)
    max_donors = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    total_amount=models.DecimalField(decimal_places=2, max_digits=9, default=0.00)
    donor_count=models.IntegerField(default=0)
    state=models.CharField(choices=State.choices(), max_length=20, default=State.active)

    def save(self, *args, **kwargs):
        created = not self.pk
        if created:
            match = Match.objects.filter(sponsor=self.sponsor, state=Match.State.active)
            if match.exists():
                match[0].state=Match.State.completed
                match[0].save()
        super().save(*args, **kwargs)


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('Sponsor', on_delete=CASCADE)
