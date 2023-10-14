"""Habitacion views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# serializers
from api.serializers.habitaciones import HabitacionModelSerializer


# Models
from api.models.habitacion import Habitacion


class HabitacionViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class = HabitacionModelSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Habitacion.objects.all()
        return queryset
