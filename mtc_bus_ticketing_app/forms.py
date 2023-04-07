from django import forms
from mtc_bus_ticketing_app.models import BusRouteDetails,BusRoutes,BookedTicketDetails

# Create your forms here.

class BusRouteDetailsForm(forms.ModelForm):
    class Meta:
        model = BusRouteDetails
        fields = '__all__'
        widgets = {
            'BusRoute': forms.TextInput(attrs={'class': 'BusRoute-field'}),
            'From': forms.TextInput(attrs={'class': 'From-field'}),
            'To': forms.TextInput(attrs={'class': 'To-field'}),
        }

class BusRoutesForm(forms.ModelForm):
    class Meta:
        model = BusRoutes
        fields = '__all__'
        widgets = {
            'BusRoute_No': forms.TextInput(attrs={'class': 'BusRoute_No-field'}),
            'Source_location': forms.TextInput(attrs={'class': 'Source_location-field'}),
            'Destination_location': forms.TextInput(attrs={'class': 'Destination_location-field'})
        }

class DeleteRouteForm(forms.ModelForm):
    class Meta:
        model = BusRouteDetails
        fields = ['BusRoute']

class UpdateRouteForm(forms.ModelForm):
    class Meta:
        model = BusRouteDetails
        fields = ['BusRoute']

class BookedTicketDetailsForm(forms.ModelForm):
    class Meta:
        model = BookedTicketDetails
        fields = ['Route_No','From_location','To_location','Ticket_Amount','No_of_Tickets','Total_Amount']