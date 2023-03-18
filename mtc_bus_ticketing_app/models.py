from django.db import models

# Create your models here.

class BusRoutes(models.Model):
    BusRoute_No = models.CharField(max_length=10, primary_key=True)
    Source_location = models.CharField(max_length=50)
    Destination_location = models.CharField(max_length=50)


class BusRouteDetails(models.Model):
    BusRoute = models.ForeignKey(BusRoutes, on_delete=models.CASCADE)
    From = models.CharField(max_length=50)
    To = models.CharField(max_length=50)
    TicketAmount = models.IntegerField()
    Duration_in_Minutes = models.IntegerField()