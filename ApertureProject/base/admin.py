from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(Airplane)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Booked)
admin.site.register(Waitlist)
admin.site.register(Bags)

