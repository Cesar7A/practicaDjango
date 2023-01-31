from django.urls import path

from . import views, include

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index')
]
