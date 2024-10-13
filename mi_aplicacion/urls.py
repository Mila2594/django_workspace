from django.urls import path
from . import views  # Asegúrate de que este archivo views.py existe en la misma carpeta

urlpatterns = [
    path('', views.index, name='index'),  # Esto mapea la URL raíz a la vista index
]
