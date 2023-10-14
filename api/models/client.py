"""  """
# Django
from django.db import models

#utilies
from api.models.base_model import BaseModel
from django.core.validators import RegexValidator

class Client(BaseModel):
    """ """

    nombre = models.CharField('nombre cliente', max_length=30)
    apellido = models.CharField(unique=True, max_length=30)

    dpi = models.CharField(unique=True, max_length=13)
    pasaporte = models.CharField(unique=True, max_length=11)
    nit = models.CharField(unique=True, max_length=11)
    telefono = models.CharField('telefono cliente', max_length=20)
    direccion = models.CharField('direccion cliente', max_length=40)
    nacionalidad = models.CharField('nacionalidad cliente', max_length=20)


    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    telefono = models.CharField(validators=[phone_regex], max_length=17, blank=True)



    def __str__(self):
        """Return circle name"""
        return self.nombre
    

