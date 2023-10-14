"""  """
# Django
from django.db import models

#utilies
from api.models.base_model import BaseModel

class Habitacion(BaseModel):
    TIPO = (
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('triple', 'Triple'),
        ('matrimonial', 'Matrimonial'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO, default='Simple')
    def _str_(self):
        """Return tipo."""
        return self.TIPO