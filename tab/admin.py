from django.contrib import admin
from .models import (Machine,Farmer,ServiceProvider,)
# Register your models here.
admin.site.register(Machine)
admin.site.register(Farmer)
admin.site.register(ServiceProvider)