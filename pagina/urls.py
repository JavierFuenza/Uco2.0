from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('registro',views.registrar,name='registro'),
    path('Nosotros',views.nosotros,name='Nosotros'),
    path('pantalones',views.pantalones,name='pantalones'),
    path('poleras',views.poleras,name='poleras'),
    path('polerones',views.polerones,name='polerones'),
]