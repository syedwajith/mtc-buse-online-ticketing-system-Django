from django.shortcuts import render,redirect
from django.contrib import messages

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

def updatebus1(request):
    return render(request, 'mtc_bus_ticketing_app/updatebus1.html')

def updatebus2(request):
    return render(request, 'mtc_bus_ticketing_app/updatebus2.html')

def deletebus(request):
    return render(request, 'mtc_bus_ticketing_app/deletebus.html')

def todaycollection(request):
    return render(request, 'mtc_bus_ticketing_app/todaycollection.html')

def overallcollection(request):
    return render(request, 'mtc_bus_ticketing_app/overallcollection.html')
