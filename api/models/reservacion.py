"""  """
# Django
from django.db import models

#utilies
from api.models.base_model import BaseModel
from api.models.client import Client
from api.models.habitacion import Habitacion

class Reservacion(BaseModel):
    """ """
    contado = "Contado"
    FORMA_PAGO = (
        ('contado', 'Contado'),
        ('tarjeta_credito', 'Tarjeta_Credito'),
    )
    

    cliente = models.OneToOneField(Client, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, null=True)
    forma_pago = models.CharField(max_length=20, choices=FORMA_PAGO, default='Contado')

    tipo_cliente = models.CharField(max_length=40)
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()
    adulto = models.PositiveBigIntegerField()
    nino = models.PositiveBigIntegerField()
    edad_nino = models.PositiveBigIntegerField()
    desayuno_buffete = models.PositiveBigIntegerField()
    dias_renta_auto = models.PositiveBigIntegerField()




    # 

    def __str__(self):
        """Return reservacion name"""
        return self.cliente.nombre
    
    # class Meta(BaseModel.Meta):
    #     """Meta class"""
    #     ordering = ['-rides_taken', '-rides_offered']
