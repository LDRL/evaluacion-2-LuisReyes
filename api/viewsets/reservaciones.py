"""Clientes views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# serializers
from api.serializers.reservaciones import ReservacionModelSerializer

# Models
from api.models.reservacion import Reservacion


class ReservacionViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Cliente view set."""

    serializer_class = ReservacionModelSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Reservacion.objects.all()
        return queryset

