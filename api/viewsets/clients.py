"""Clientes views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# serializers
from api.serializers.clients import ClientModelSerializer

# Models
from api.models.client import Client


class ClientViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Cliente view set."""

    serializer_class = ClientModelSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Client.objects.all()
        return queryset

    # def get_permissions(self):
    #     """Assign permissions based on action"""
    #     permissions = [IsAuthenticated]
    #     if self.action in ['update', 'partial_update']:
    #         permissions.append(IsCircleAdmin)
    #     return [permission() for permission in permissions]

    # def perform_create(self, serializer):
    #     """Assign circle admin"""
    #     circle = serializer.save()
    #     user = self.request.user
    #     profile = user.profile
    #     Membership.objects.create(
    #         user=user,
    #         profile=profile,
    #         circle=circle,
    #         is_admin=True,
    #         remaining_invitations=10
    #     )
