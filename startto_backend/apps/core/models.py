from django.db import models
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator, MinValueValidator
from startto_backend.storage_backends import MediaStorage

# Create your models here.

class Location(models.Model):
    street_address = models.CharField(max_length=256, blank=True)
    address_notes = models.CharField(max_length=256, blank=True)
    property_description = models.CharField(max_length=256, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    ward=models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(25)
        ]
    )
    old_ward=models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(50)
        ]
    )
    neighbourhood=models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.street_address


class Label(models.Model):
    label_text = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.label_text

    def __unicode__(self):
        return self.label_text


class Category(models.Model):
    name = models.CharField(max_length=128)
    submittable_id = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ImageAttachment(models.Model):
    file = ResizedImageField(
        blank=False,
        null=False,
        storage=MediaStorage(),
        max_length=200,
        size=[250, 250],
        crop=['middle', 'center'],
        quality=99
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )



