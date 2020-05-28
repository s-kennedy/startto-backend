# Django
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404

# App
from startto_backend.apps.artworks.api.serializers import (
    SubmissionSerializer,
    ArtworkSerializer,
)
from startto_backend.apps.artworks.models import Submission, Artwork

# Rest Framework
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions


# class UpdatePermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         submitted_id = request.data.get('id')
#         if view.action == 'update' and submitted_id != request.user.id:
#             return False
#         if view.action == 'destroy' and submitted_id != request.user.id:
#             return False
#         return True


# class ModifyFeaturedTalkPermissions(permissions.BasePermission):
#     def has_permission(self, request, view):
#         profile_id = request.data.get('profile')
#         if view.action == 'create' and profile_id != request.user.id:
#             return False
#         if view.action == 'update' and profile_id != request.user.id:
#             return False
#         if view.action == 'destroy' and profile_id != request.user.id:
#             return False
#         return True

# class UpdateProfilePermissions(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if obj.published == False and obj.user.pk != request.user.id:
#             return False
#         return True


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     http_method_names = ['get', 'post', 'put', 'delete']
#     permission_classes = (UpdatePermissions,)

#     def get_queryset(self):
#         if not self.request.user.is_authenticated:
#             return User.objects.none()
#         return User.objects.filter(
#             id=self.request.user.id
#         ).all()


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Submission.objects.all().order_by("-pk")
        return queryset

    def get_object(self):
        queryset = Profile.objects.all()

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class ArtworkViewSet(viewsets.ModelViewSet):
    serializer_class = ArtworkSerializer

    def get_queryset(self):
        queryset = Artwork.objects.all().order_by("-pk")

        if 'offset' in self.request.GET or 'limit' in self.request.GET:
            limit = int(self.request.query_params.get('limit', 20))
            offset = int(self.request.query_params.get('offset', 0))
            queryset = queryset[offset:offset+limit]

        return queryset


