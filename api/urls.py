from api import viewsets
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r"clientes",viewsets.ClientViewSet, "clientes")
router.register(r"habitaciones",viewsets.HabitacionViewSet, "habitaciones")
router.register(r"reservaciones",viewsets.ReservacionViewSet, "reservaciones")

urlpatterns = [
    path(r"", include(router.urls)),
]
