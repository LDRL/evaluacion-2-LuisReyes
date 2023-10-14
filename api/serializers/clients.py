"""Client serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from api.models.client import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """Client model serializer."""

    # members_limit = serializers.IntegerField(
    #     required=False,
    #     min_value = 10,
    #     max_value = 32000
    # )
    # is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class."""

        model = Client
        fields = (
            'nombre', 'apellido',
            'direccion', 'dpi',
            'pasaporte','nit', 'telefono',
            'direccion', 'nacionalidad','email',
        )

        # read_only_fields = (
        #     'is_public',
        #     'verified',
        #     'rides_offered',
        #     'rides_taken'
        # )

    # def validate(self, data):

    #     """Ensure both members_limit """
    #     members_limit = data.get('members_limit', None)
    #     is_limited = data.get('is_limited',False)
    #     if is_limited ^ bool(members_limit):
    #         raise serializers.ValidationError('If Client is limited, a member limit mus be provided')
    #     return data