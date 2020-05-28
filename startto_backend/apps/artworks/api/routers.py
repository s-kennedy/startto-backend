# App
from startto_backend.apps.artworks.api.viewsets import ArtworkViewSet, SubmissionViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'artworks', ArtworkViewSet, basename='artwork')
router.register(r'submissions', SubmissionViewSet, basename='submission')