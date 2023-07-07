from django.contrib import admin
from .models import producto,compra,categoria,imagen

# Register your models here.
admin.site.register(producto)
admin.site.register(compra)
admin.site.register(categoria)
admin.site.register(imagen)
