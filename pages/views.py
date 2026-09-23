from django.shortcuts import render
from listings.models import Listing

def home(request):
    listings = Listing.objects.filter(
        status='approved'
    ).order_by('start_date')

    context = {
        'listings': listings,
    }

    return render(request, 'pages/home.html', context)
