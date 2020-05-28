from django.shortcuts import render
from django.views import View
from django import http
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal

from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.artworks.models import Artwork
from startto_backend.apps.core.models import Location, Program

import json


def json_response(objects):
    data = json.dumps(objects, cls=DjangoJSONEncoder)
    return http.HttpResponse(data, 'application/json')

def parse_coordinates(lat, lon):
    if type(lat) is not Decimal or type(lon) is not Decimal:
        return None
    if lon > 180 or lon < -180 or lat > 90 or lat < -90:
        return None
    return [lon,lat]


class MapFeaturesView(View):
    def get(self, request):
        data = {
            "crs": {
                "properties": {
                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                },
                "type": "name"
            },
            "type": "FeatureCollection",
            "features": []
        }

        artworks = Artwork.objects.select_related('location', 'program').all()

        for item in artworks:
            feature = {
                "type": "Feature",
                "id": item.uid,
                "properties": {
                    "title": item.title,
                    "description": item.description,
                    "artist": item.artist_credit,
                    "address": item.location.street_address,
                    "yr": item.year,
                    "partner": item.partner,
                    "ward": item.location.ward,
                    "prgrm": item.program.name if item.program else None,
                    "medium": item.medium,
                    "uid": item.uid,
                }
            }

            coordinates = parse_coordinates(item.location.latitude, item.location.longitude)

            if coordinates is not None:
                feature["geometry"] = {
                    "type": 'Point',
                    "coordinates": coordinates
                }

            data["features"].append(feature)

        return json_response(data)