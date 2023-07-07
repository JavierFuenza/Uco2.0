from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='Index'),
    path('registro',views.registro,name='registro'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('pantalones',views.pantalones,name='pantalones'),
    path('poleras',views.poleras,name='poleras'),
    path('ropa',views.polerones,name='ropa'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('datos-modelo', views.obtener_datos_modelo, name='datos-modelo')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
