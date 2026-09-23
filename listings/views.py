from django.shortcuts import render
from .models import Listing

def listing_list(request):

    listings = Listing.objects.filter(
        status="approved"
    ).order_by("start_date")

    context = {
        "listings": listings,
    }

    return render(request, "listings/list.html", context)
