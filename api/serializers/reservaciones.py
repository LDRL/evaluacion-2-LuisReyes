"""Client serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from api.models.reservacion import Reservacion


class ReservacionModelSerializer(serializers.ModelSerializer):
    """Client model serializer."""

    class Meta:
        """Meta class."""

        model = Reservacion
        fields = (
            'cliente', 'tipo_cliente',
            'fecha_hora_entrada', 'fecha_hora_salida',
            'adulto', 'nino', 'edad_nino', 'desayuno_buffete',
            'dias_renta_auto'
           
        )