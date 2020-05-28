# Django
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

import uuid
import requests

# App
from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.artworks.models import Artwork
from startto_backend.apps.core.models import Category


def get_json_response(url):
    response = requests.get(url)
    try:
        return response.json()
    except:
        raise ConnectionError("Request to {} returned {}".format(url, response.status_code))


class Command(BaseCommand):
    help = "Import categories from Submittable."

    def get_or_create_categories(self):
        endpoint = "https://api.submittable.com/v1/categories?count=200"
        response = requests.get(endpoint, auth=(settings.SUBMITTABLE_ACCESS_TOKEN, '')).json()

        self.stdout.write(self.style.SUCCESS('GOT CATEGORIES!'))

        for category in response["items"]:

            category_exists = Category.objects.filter(submittable_id=category["category_id"]).exists()

            if not category_exists:

                # create category
                category = Category.objects.create(
                    submittable_id=category["category_id"],
                    name=category["name"],
                    description=category["description"],
                )

                self.stdout.write(self.style.SUCCESS("Added category: {}".format(category.name)))

    def handle(self, *args, **options):
        self.get_or_create_categories()
        self.stdout.write(self.style.SUCCESS('=== Successfully imported categories! ==='))
