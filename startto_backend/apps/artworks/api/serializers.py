# Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings

# App
from startto_backend.apps.artworks.models import Submission, Artwork
from startto_backend.apps.core.api.serializers import LocationSerializer, ProgramSerializer

# Rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)
        return data


class ArtworkSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Artwork
        fields = '__all__'
