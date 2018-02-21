import os

from django.http import HttpResponseRedirect

from .models import test

from django.shortcuts import render

def get_sponsor():
    return test.User.objects.get(username='Carl').sponsor

def get_donor():
    return test.User.objects.get(username='Tim').donor

def sponsor(request):
    return render(request, 'sponsor.html', {
        'donations': test.Donation.objects.all(),
        'match': get_sponsor().match
    })

def sponsor_post(request):
    post = request.POST
    days = post.get('days', None)
    amount = post.get('amount', None)
    test.Match(
        days=days,
        amount=amount,
        sponsor=get_sponsor()
    ).save()
    return HttpResponseRedirect('/sponsor')

def donor(request):
    return render(request, 'donor.html', {
        'donations': test.Donation.objects.all()
    })

def donor_post(request):
    post = request.POST
    amount = post.get('amount', None)
    test.Donation(
        amount=amount,
        donor=get_donor(),
        campaign=test.Campaign.objects.all()[0]
    ).save()
    return HttpResponseRedirect('/donor')
