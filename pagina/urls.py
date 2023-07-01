from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('registro',views.registro,name='registro'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('pantalones',views.pantalones,name='pantalones'),
    path('poleras',views.poleras,name='poleras'),
    path('polerones',views.polerones,name='polerones'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
]