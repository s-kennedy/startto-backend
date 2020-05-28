from django.shortcuts import render
from django.views import View

from django import http
from django.core.serializers.json import DjangoJSONEncoder

from startto_backend.apps.accounts.models import Profile
from startto_backend.apps.artworks.models import Artwork, Submission


import json

def json_response(objects):
    data = json.dumps(objects, cls=DjangoJSONEncoder)
    return http.HttpResponse(data, 'application/json')

class StatsView(View):
    def get(self, request):
        data = { "artworks": {}, "artists": {}, "submissions": {} }

        artist_count = Profile.objects.count()
        artwork_count = Artwork.objects.count()
        submission_count = Submission.objects.count()

        data["artists"] = { "count": artist_count }
        data["artworks"] = { "count": artwork_count }
        data["submissions"] = { "count": submission_count }

        return json_response(data)

