from django.shortcuts import render
from datetime import date, timedelta
from listings.models import Listing

def home(request):
    today = date.today()
    week_ahead = today + timedelta(days=7)

    listings = Listing.objects.filter(
        status='approved',
        start_date__gte=today,
        start_date__lte=week_ahead
    ).order_by('start_date')

    context = {
        'listings': listings,
    }

    return render(request, 'pages/home.html', context)
