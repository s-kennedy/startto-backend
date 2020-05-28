# Django
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

import uuid
import requests
from datetime import datetime

# third party
from airtable import Airtable

# App
from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.artworks.models import Artwork, Submission
from startto_backend.apps.core.models import Location, Program


def get_json_response(url):
    response = requests.get(url)
    try:
        return response.json()
    except:
        raise ConnectionError("Request to {} returned {}".format(url, response.status_code))



class Command(BaseCommand):
    help = "Import artworks from Airtable."

    def import_airtable_records(self):
        airtable = Airtable(settings.AIRTABLE_BASE_ID, settings.AIRTABLE_DATA_TABLE, api_key=settings.AIRTABLE_API_KEY)
        records = airtable.get_all()

        for item in records:

            uid = item["fields"]["uid"] if item["fields"]["uid"] else uuid.uuid4()

            if Artwork.objects.filter(uid=uid).exists():
                continue

            # create or get location
            street_address = item["fields"].get("address", "")
            latitude = item["fields"].get("lat", None)
            longitude = item["fields"].get("lon", None)

            location = Location.objects.filter(street_address=street_address, longitude=longitude, latitude=latitude).first()

            if location is None:
                location = Location.objects.create(
                    street_address = street_address,
                    ward = item["fields"].get("ward", None),
                    old_ward = item["fields"].get("old_ward", None),
                    latitude = latitude,
                    longitude = longitude,
                    neighbourhood = item["fields"].get("neighbourhood", ""),
                    property_description = item["fields"].get("prp_desc", ""),
                    address_notes = item["fields"].get("adr_notes", ""),
                )

            # get program
            prgrm_field = item["fields"].get("prgrm", None)
            program = Program.objects.filter(name=prgrm_field).first() if prgrm_field else None


            # create artwork
            yr_field = item["fields"].get("yr", None)
            year = int(yr_field) if yr_field else datetime.now().year
            artwork = Artwork.objects.create(
                uid = uid,
                airtable_id = item["id"],
                description = item["fields"].get("description", ""),
                partner = item["fields"].get("partner", ""),
                medium = item["fields"].get("medium", ""),
                width = item["fields"].get("width", ""),
                height = item["fields"].get("height", ""),
                sqft = item["fields"].get("sqft", None),
                year = year,
                artist_credit = item["fields"].get("artist", ""),
                program = program,
                location = location,
            )

            self.stdout.write(self.style.SUCCESS("Added artwork by {} at {}".format(artwork.artist_credit, artwork.location)))

    def handle(self, *args, **options):
        self.import_airtable_records()
        self.stdout.write(self.style.SUCCESS('=== Successfully imported artworks from Airtable! ==='))
