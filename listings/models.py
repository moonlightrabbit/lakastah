from django.db import models

class Listing(models.Model):

    CATEGORY_CHOICES = [
        ("event", "Event"),
        ("volunteer", "Volunteer"),
        ("workshop", "Workshop"),
        ("competition", "Competition"),
        ("course", "Course"),
        ("community", "Community"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField()

    organiser_name = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    start_date = models.DateField()

    start_time = models.TimeField(
        null=True,
        blank=True,
    )

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    end_time = models.TimeField(
        null=True,
        blank=True,
    )

    registration_url = models.URLField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title