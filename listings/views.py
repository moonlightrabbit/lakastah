from django.shortcuts import render
from datetime import date
from .models import Listing

def listing_list(request):
    today = date.today()

    listings = Listing.objects.filter(
        status="approved",
        start_date__gte=today
    ).order_by("start_date")

    context = {
        "listings": listings,
    }

    return render(request, "listings/list.html", context)
