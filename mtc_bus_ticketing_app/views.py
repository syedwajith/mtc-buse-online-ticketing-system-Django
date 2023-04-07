from django.shortcuts import render,redirect
from django.contrib import messages
from mtc_bus_ticketing_app.forms import BusRouteDetailsForm,BusRoutesForm,DeleteRouteForm,UpdateRouteForm
from mtc_bus_ticketing_app.models import BusRouteDetails,BusRoutes,BookedTicketDetails
import datetime

# Create your views here.

def index(request):
    return render(request, 'mtc_bus_ticketing_app/index.html')

def adminlogin(request):
    if request.method == 'POST':
        adminuser = request.POST.get('adminuser')
        adminpassword = request.POST.get('adminpassword')
        if len(adminuser) == 0 or len(adminpassword) == 0:
            messages.error(request, 'Please fill the fields')
        elif adminuser == 'admin' and adminpassword == 'admin':
            return redirect('/mtc_bus_ticketing_app/adminhome')
        else:
            messages.error(request, 'Please enter the valid values')
    return render(request, 'mtc_bus_ticketing_app/adminlogin.html')

def adminhome(request):
    return render(request, 'mtc_bus_ticketing_app/adminhome.html')

def addbus(request):
    return render(request, 'mtc_bus_ticketing_app/addbus.html')

def busroutes(request):
    form = BusRoutesForm()
    if request.method == 'POST':
        form = BusRoutesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datas are Saved Successfully')
            return redirect('/mtc_bus_ticketing_app/busroutes')
    return render(request, 'mtc_bus_ticketing_app/busroutes.html', {'form':form})

def routedetails(request):
    form = BusRouteDetailsForm()
    if request.method == 'POST':
        form = BusRouteDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datas are Saved Successfully')
            return redirect('/mtc_bus_ticketing_app/routedetails')
    return render(request, 'mtc_bus_ticketing_app/routedetails.html', {'form':form})

def updatebus1(request):
    form = UpdateRouteForm()
    if request.method == 'POST':
        form = UpdateRouteForm(request.POST)
        if form.is_valid():
            BusRoute_No = form.cleaned_data['BusRoute_No']
            busroutedetails = BusRouteDetails.objects.filter(BusRoute=BusRoute_No)
            if busroutedetails.exists():
                if busroutedetails and hasattr(busroutedetails, 'busroutedetail'):
                    context = {'busroutedetail':busroutedetails.busroutedetail}
                    return render(request, 'mtc_bus_ticketing_app/updatebus2.html', context)
            else:
                messages.error(request, 'No results found')
    return render(request, 'mtc_bus_ticketing_app/updatebus1.html', {'form':form})

def updatebus2(request):
    busroutedetail = request.GET.get('busroutedetail')
    context = {'busroutedetail':busroutedetail}
    return render(request, 'mtc_bus_ticketing_app/updatebus2.html', context)

def deletebus(request):
    form = DeleteRouteForm()
    if request.method == 'POST':
        form = DeleteRouteForm(request.POST)
        if form.is_valid():
            BusRoute_No = form.cleaned_data['BusRoute_No']
            busroutes = BusRoutes.objects.get(BusRoute_No=BusRoute_No)
            busroute_detail = BusRouteDetails.objects.filter(BusRoute=BusRoute_No)
            if busroutes.exists() or busroute_detail.exists():
                busroutes.delete()
                busroute_detail.delete()
                messages.success(request, 'Datas are Deleted Successfully')
                return redirect('/mtc_bus_ticketing_app/deletebus')
            else:
                messages.error(request, 'No results found')
    return render(request, 'mtc_bus_ticketing_app/deletebus.html', {'form':form})

def viewbusroutes(request):
    busdetails = BusRoutes.objects.all()
    return render(request, 'mtc_bus_ticketing_app/viewbusroutes.html', {'busdetails':busdetails})

def todaycollection(request):
    return render(request, 'mtc_bus_ticketing_app/todaycollection.html')

def overallcollection(request):
    return render(request, 'mtc_bus_ticketing_app/overallcollection.html')