# Django
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import csv
import uuid

# App
from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.core.models import Location, Topic


class Command(BaseCommand):
    help = "Import users from CSV file. Usage: python manage.py import_users '/path/to/file.csv'"

    def get_or_create_users(self, csv_file):
        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            for row in reader:
                # check if user exists
                email = row[9].strip()
                user_exists = User.objects.filter(email=email).exists()

                if not user_exists:

                    # create user and profile
                    user = User.objects.create_user(
                        email,
                        email,
                        uuid.uuid4()
                    )

                    user.save()
                else:
                    user = User.objects.filter(email=email)[0]

                # populate profile
                user.profile.first_name = row[4]
                user.profile.last_name = row[5]
                user.profile.position = row[6]
                user.profile.organization = row[7]
                user.profile.twitter = row[8]

                identities = row[10].split('|')

                user.profile.poc = 'Person of Color' in identities
                user.profile.woman = 'Woman' in identities

                # use image on AWS bucket
                wp_image_location = row[3]
                filename = wp_image_location.split('/')[-1]
                aws_location = settings.MEDIA_URL + filename
                user.profile.image = aws_location

                # add location to profile
                location = Location.objects.get(city='Toronto')
                user.profile.location = location

                # add topics to profile
                tags = row[11].split('|')
                for tag in tags:
                    topic, _created = Topic.objects.get_or_create(topic=tag)
                    user.profile.topics.add(topic)

                # set profile status as approved
                user.profile.status = Profile.APPROVED

                user.profile.save()
                self.stdout.write(self.style.SUCCESS('Created or updated user {}'.format(user.profile.first_name)))

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        csv_file = options['file']
        self.get_or_create_users(csv_file)

        self.stdout.write(self.style.SUCCESS('=== Successfully imported users! ==='))
