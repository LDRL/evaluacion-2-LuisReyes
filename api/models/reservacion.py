"""  """
# Django
from django.db import models

#utilies
from api.models.base_model import BaseModel
from api.models.client import Client

class Reservacion(BaseModel):
    """ """

    cliente = models.OneToOneField(Client, on_delete=models.CASCADE)
    # forma_pago = models.ImageField(unique=True, max_length=11)
    tipo_cliente = models.CharField(max_length=40)
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()
    adulto = models.PositiveBigIntegerField()
    nino = models.PositiveBigIntegerField()
    edad_nino = models.PositiveBigIntegerField()
    desayuno_buffete = models.PositiveBigIntegerField()
    dias_renta_auto = models.PositiveBigIntegerField()

    def __str__(self):
        """Return circle name"""
        return self.cliente.nombre
    
    # class Meta(BaseModel.Meta):
    #     """Meta class"""
    #     ordering = ['-rides_taken', '-rides_offered']
