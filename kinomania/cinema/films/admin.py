from django.contrib import admin
from .models import Film,Hall,Screening,Ticket

admin.site.register(Film)
admin.site.register(Hall)
admin.site.register(Screening)
admin.site.register(Ticket)
