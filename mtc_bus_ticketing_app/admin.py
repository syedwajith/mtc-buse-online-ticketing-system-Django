from django.contrib import admin
from mtc_bus_ticketing_app.models import BusRouteDetails,BusRoutes,BookedTicketDetails

# Register your models here.

class BusRoutesAdmin(admin.ModelAdmin):
    list = ['BusRoute_No','Source_location','Destination_location']

admin.site.register(BusRoutes,BusRoutesAdmin)

class BusRouteDetailsAdmin(admin.ModelAdmin):
    list = ['BusRoute','From','To','TicketAmount','Duration_in_Minutes']

admin.site.register(BusRouteDetails,BusRouteDetailsAdmin)

class BookedTicketDetailsAdmin(admin.ModelAdmin):
    list = ['Route_No','From_location','To_location','Ticket_Amount','No_of_Tickets','Total_Amount','Booked_Date','Expired_Date']

admin.site.register(BookedTicketDetails,BookedTicketDetailsAdmin)