from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator, MinValueValidator

from startto_backend.storage_backends import MediaStorage
from startto_backend.apps.core.models import Location, ImageAttachment, Label, Category, Program

from datetime import datetime

class Submission(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In-Progress'
    WITHDRAWN = 'Withdrawn'
    ACCEPTED = 'Accpeted'
    DECLINED = 'Declined'

    STATUS_OPTIONS = (
        (NEW, NEW),
        (IN_PROGRESS, IN_PROGRESS),
        (WITHDRAWN, WITHDRAWN),
        (ACCEPTED, ACCEPTED),
        (DECLINED, DECLINED),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_OPTIONS,
        default=NEW
    )

    submittable_url = models.URLField(max_length=256)

    submittable_id = models.CharField(max_length=128)

    title = models.CharField(max_length=256)

    description = models.TextField(blank=True)

    organization_name = models.CharField(max_length=256, blank=True)

    organization_website = models.URLField(blank=True)

    is_archived = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    labels = models.ManyToManyField(
        Label
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class Artwork(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    airtable_id = models.CharField(
        max_length=256,
        blank=True
    )

    uid = models.CharField(
        max_length=256,
        blank=True
    )

    title = models.CharField(
        max_length=256,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    partner = models.CharField(
        max_length=256,
        blank=True
    )

    medium = models.CharField(
        max_length=256,
        blank=True
    )

    width = models.CharField(
        max_length=128,
        blank=True
    )

    height = models.CharField(
        max_length=128,
        blank=True
    )

    artist_credit = models.CharField(
        max_length=256,
        blank=True
    )

    sqft = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True,
        blank=True
    )

    year = models.IntegerField(
        default=datetime.now().year,
        validators=[
            MaxValueValidator(2012),
            MinValueValidator(2030)
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

