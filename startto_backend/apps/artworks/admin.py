from django.contrib import admin

# App
from startto_backend.apps.artworks.models import (
    Artwork,
    Submission
)

# Register your models here.
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'submittable_id',
        'user',
        'title',
        'status',
        'is_archived',
        'category'
    ]

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'uid',
        'artist_credit',
        'description',
        'location',
    ]