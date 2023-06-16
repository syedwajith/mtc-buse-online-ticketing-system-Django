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
            'Destination_location': forms.TextInput(attrs={'class': 'Destination_location-field'}),
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
        widgets = {
            'Route_No': forms.TextInput(attrs={'readonly': 'readonly'}),
            'From_location': forms.TextInput(attrs={'readonly': 'readonly'}),
            'To_location': forms.TextInput(attrs={'readonly': 'readonly'}),
            'Ticket_Amount': forms.NumberInput(attrs={'readonly': 'readonly','id': 'ticket_amt'}),
            'No_of_Tickets': forms.NumberInput(attrs={'id': 'no_ticket'}),
            'Total_Amount': forms.NumberInput(attrs={'id': 'tot_amt', 'readonly': 'readonly'}),
        }

class RouteSerchForm(forms.ModelForm):
    class Meta:
        model = BusRouteDetails
        fields = ['From','To']

class RouteNoSearchForm(forms.ModelForm):
    class Meta:
        model = BusRouteDetails
        fields = ['BusRoute']