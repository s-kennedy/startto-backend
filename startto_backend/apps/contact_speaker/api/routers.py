# App
from startto_backend.apps.contact_speaker.api.viewsets import ContactFormViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'contact_form', ContactFormViewSet, basename='contact_form')