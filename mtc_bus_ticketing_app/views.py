from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'mtc_bus_ticketing_app/index.html')

def adminlogin(request):
    return render(request, 'mtc_bus_ticketing_app/adminlogin.html')