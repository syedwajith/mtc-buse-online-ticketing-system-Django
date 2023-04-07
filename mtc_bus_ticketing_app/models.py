from django.db import models

# Create your models here.

class BusRoutes(models.Model):
    BusRoute_No = models.CharField(max_length=10, unique=True)
    Source_location = models.CharField(max_length=50)
    Destination_location = models.CharField(max_length=50)


class BusRouteDetails(models.Model):
    BusRoute = models.CharField(max_length=10)
    From = models.CharField(max_length=50)
    To = models.CharField(max_length=50)
    TicketAmount = models.FloatField()
    Duration_in_Minutes = models.IntegerField()

class BookedTicketDetails(models.Model):
    Route_No = models.CharField(max_length=10)
    From_location = models.CharField(max_length=50)
    To_location = models.CharField(max_length=50)
    Ticket_Amount = models.FloatField()
    No_of_Tickets = models.IntegerField()
    Total_Amount = models.FloatField()
    Booked_Date = models.DateTimeField()
    Expired_Date = models.DateTimeField()