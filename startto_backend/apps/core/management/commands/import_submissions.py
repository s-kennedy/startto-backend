# Django
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

import uuid
import requests

# App
from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.artworks.models import Submission
from startto_backend.apps.core.models import Category


def get_json_response(url):
    response = requests.get(url)
    try:
        return response.json()
    except:
        raise ConnectionError("Request to {} returned {}".format(url, response.status_code))


class Command(BaseCommand):
    help = "Import submissions from Submittable."

    def get_or_create_submissions(self):
        endpoint = "https://api.submittable.com/v1/submissions?count=200"
        response = requests.get(endpoint, auth=(settings.SUBMITTABLE_ACCESS_TOKEN, '')).json()

        self.stdout.write(self.style.SUCCESS('GOT SUBMISSIONS!'))

        for item in response["items"]:

            submission_exists = Submission.objects.filter(submittable_id=item["submission_id"]).exists()

            if not submission_exists:

                # create or retrieve user
                email = item["submitter"]["email"]

                if email is None:
                    continue

                email = email.lower()
                user = User.objects.filter(email=email).first()

                if user is None:
                    user = User.objects.create_user(
                        email,
                        email,
                        uuid.uuid4()
                    )

                    user.save()

                    # populate profile
                    user.profile.submittable_id = item["submitter"]["user_id"]
                    user.profile.first_name = item["submitter"]["first_name"]
                    user.profile.last_name = item["submitter"]["last_name"]
                    user.profile.phone_number = item["submitter"]["phone"]

                    self.stdout.write(self.style.SUCCESS("Added artist: {}".format(user.profile)))

                # create record for submission
                submission = Submission.objects.create(
                    submittable_id=item["submission_id"],
                    submittable_url=item["url"],
                    status=item["status"],
                    title=item["title"],
                    is_archived=item["is_archived"],
                    user=user
                )

                # add category
                category_submittable_id = item["category"]["category_id"]
                category = Category.objects.filter(submittable_id=category_submittable_id).first()
                submission.category = category
                submission.save()

                self.stdout.write(self.style.SUCCESS("Added submission: {} for {}".format(submission, category)))


    def handle(self, *args, **options):
        self.get_or_create_submissions()
        self.stdout.write(self.style.SUCCESS('=== Successfully imported submissions! ==='))
