from django.contrib import admin
from mtc_bus_ticketing_app.models import BusRouteDetails

# Register your models here.

class BusRouteAdmin(admin.ModelAdmin):
    list = ['BusRoute','From','To','TicketAmount','Duration_in_Minutes']

admin.site.register(BusRouteDetails,BusRouteAdmin)