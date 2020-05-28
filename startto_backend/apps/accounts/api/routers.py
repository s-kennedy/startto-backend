# App
from startto_backend.apps.accounts.api.viewsets import UserViewSet, ProfileViewSet, ImageUploadViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'images', ImageUploadViewSet, basename='image')