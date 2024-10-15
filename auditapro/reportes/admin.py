from django.contrib import admin


# Register your models here.

from .models import Cliente, Usuario, Camera, Light

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Camera)
admin.site.register(Light)