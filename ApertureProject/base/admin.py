from django.contrib import admin
from .models import Airplane,Flight,Ticket
# Register your models here.

admin.site.register(Airplane)
admin.site.register(Flight)
admin.site.register(Ticket)

