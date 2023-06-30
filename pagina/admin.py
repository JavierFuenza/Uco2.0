from django.contrib import admin
from .models import user,producto,compra

# Register your models here.
admin.site.register(user)
admin.site.register(producto)
admin.site.register(compra)
