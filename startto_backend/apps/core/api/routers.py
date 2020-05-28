# App
from startto_backend.apps.core.api.viewsets import LocationViewSet, TopicViewSet, SubscriptionGroupViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)
router.register(r'topics', TopicViewSet, basename="topic")
router.register(r'subscription_groups', SubscriptionGroupViewSet, basename="subscription_group")
