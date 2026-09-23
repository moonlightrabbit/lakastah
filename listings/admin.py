from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "organiser_name",
        "start_date",
        "status",
    )

    list_filter = (
        "category",
        "status",
        "start_date",
    )

    search_fields = (
        "title",
        "organiser_name",
        "description",
    )
