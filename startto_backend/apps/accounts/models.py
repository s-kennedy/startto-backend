from django.contrib.auth.models import User
from django.db import models

# App
from startto_backend.storage_backends import MediaStorage
from django_resized import ResizedImageField


class Profile(models.Model):
    """
    Extends from the user model
    """
    HE = 'he'
    SHE = 'she'
    THEY = 'they'
    PRONOUNS_CHOICE = (
        (HE, HE),
        (SHE, SHE),
        (THEY, THEY)
    )

    submittable_id = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    image = models.CharField(
        max_length=5000,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    pronouns = models.CharField(
        max_length=10,
        choices=PRONOUNS_CHOICE,
        null=True,
        blank=True
    )

    organization = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    bio = models.CharField(
        max_length=1024,
        null=True,
        blank=True
    )

    social_media = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    website = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def display_name(self):
        first_name = self.first_name
        last_name = self.last_name

        if first_name and last_name:
            return u"%s %s".strip() % (first_name, last_name)

        return None

    def __str__(self):
        return self.display_name()

    def __unicode__(self):
        return self.display_name()



class ImageUpload(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

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

