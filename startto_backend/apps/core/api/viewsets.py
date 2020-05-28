# App
from startto_backend.apps.core.api.serializers import LocationSerializer
from startto_backend.apps.core.models import Location
from startto_backend.apps.accounts.models import Profile

# Rest Framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.order_by('street_address')
    serializer_class = LocationSerializer

