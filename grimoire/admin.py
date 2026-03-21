from django.contrib import admin
from .models import Pessoa, Casa

admin.site.register(Pessoa) #Admin - User: user / Password: 123
admin.site.register(Casa)

# Register your models here.
