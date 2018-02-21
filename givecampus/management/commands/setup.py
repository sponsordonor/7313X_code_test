from givecampus.models import test

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation


class Command(BaseCommand):

    def handle(self, *args, **options):

        carl, created = test.User.objects.get_or_create(
            username='Carl'
        )
        tim, created = test.User.objects.get_or_create(
            username='Tim'
        )
        sponsor = test.Sponsor()
        sponsor.save()
        carl.sponsor = sponsor
        carl.save()

        donor = test.Donor()
        donor.save()
        tim.donor = donor
        tim.save()


        campaign, created = test.Campaign.objects.get_or_create(
            name='Carl College Fundraiser',
            owner=carl.sponsor
        )

        donation, created = test.Donation.objects.get_or_create(
            title='Carl',
            description='DDD',
            amount=99.33,
            campaign=campaign,
            donor=tim.donor
        )
        print(donation.amount)