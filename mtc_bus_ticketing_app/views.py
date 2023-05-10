from django.shortcuts import render,redirect
from django.contrib import messages
from mtc_bus_ticketing_app.forms import BusRouteDetailsForm,BusRoutesForm,DeleteRouteForm,UpdateRouteForm
from mtc_bus_ticketing_app.models import BusRouteDetails,BusRoutes,BookedTicketDetails
import datetime

# Main Home Page

def index(request):
    return render(request, 'mtc_bus_ticketing_app/index.html')

# Admin Site

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
            BusRoute = form.cleaned_data['BusRoute']
            busroutedetails = BusRouteDetails.objects.filter(BusRoute=BusRoute)
            if busroutedetails.exists():
                busroutedetail = BusRouteDetails.objects.filter(BusRoute=BusRoute).values('BusRoute','From','To','TicketAmount')
                return render(request, 'mtc_bus_ticketing_app/updatebus2.html', {'busroutedetail':busroutedetail})
            else:
                messages.error(request, 'No results found')
    return render(request, 'mtc_bus_ticketing_app/updatebus1.html', {'form':form})

def updatebus2(request):
    busroutedetail = request.GET.getlist('busroutedetail')
    return render(request, 'mtc_bus_ticketing_app/updatebus2.html', {'busroutedetail':busroutedetail})

def updatebus2_update(request,id):
    update = BusRouteDetails.objects.get(id=id)
    if request.method == 'POST':
        form = BusRouteDetailsForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect('/mtc_bus_ticketing_app/updatebus2')
    return render(request, 'mtc_bus_ticketing_app/updatebus3.html', {'update':update})

def updatebus3(request):
    return render(request, 'mtc_bus_ticketing_app/updatebus3.html')

def deletebus(request):
    form = DeleteRouteForm()
    if request.method == 'POST':
        form = DeleteRouteForm(request.POST)
        if form.is_valid():
            BusRoute = form.cleaned_data['BusRoute']
            busroutes = BusRoutes.objects.filter(BusRoute_No=BusRoute)
            busroute_detail = BusRouteDetails.objects.filter(BusRoute=BusRoute)
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

# Passenger Site