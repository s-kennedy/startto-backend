# Django
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

# App
from startto_backend.apps.accounts.models import Profile
from mailchimp3 import MailChimp

import hashlib
import requests

speaker_approved = Signal(providing_args=["profile"])


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))

