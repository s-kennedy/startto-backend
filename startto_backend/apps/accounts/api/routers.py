# App
from startto_backend.apps.accounts.api.viewsets import UserViewSet, ProfileViewSet, ImageUploadViewSet, FeaturedTalkViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'images', ImageUploadViewSet, basename='image')
router.register(r'featured_talks', FeaturedTalkViewSet, basename='featured_talk')