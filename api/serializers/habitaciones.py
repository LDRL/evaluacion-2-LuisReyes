"""Client serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from api.models.habitacion import Habitacion


class HabitacionModelSerializer(serializers.ModelSerializer):
    """Habitacion model serializer."""

    class Meta:
        """Meta class."""

        model = Habitacion
        

    # def validate(self, data):

    #     """Ensure both members_limit """
    #     members_limit = data.get('members_limit', None)
    #     is_limited = data.get('is_limited',False)
    #     if is_limited ^ bool(members_limit):
    #         raise serializers.ValidationError('If Client is limited, a member limit mus be provided')
    #     return data