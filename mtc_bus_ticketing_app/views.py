from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from mtc_bus_ticketing_app.forms import BusRouteDetailsForm, BusRoutesForm, DeleteRouteForm, UpdateRouteForm, RouteSerchForm, RouteNoSearchForm, BookedTicketDetailsForm
from mtc_bus_ticketing_app.models import BusRouteDetails, BusRoutes, BookedTicketDetails
from datetime import datetime, timedelta, date

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
                return render(request, 'mtc_bus_ticketing_app/updatebus2.html', {'busroutedetail':busroutedetails})
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
            messages.success(request, 'Datas are updated successfully')
            return redirect('/mtc_bus_ticketing_app/updatebus1')
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
    today_date = date.today()
    total_amount = BookedTicketDetails.objects.filter(Booked_Date__date=today_date).values('Route_No').annotate(total=Sum('Total_Amount'))
    return render(request, 'mtc_bus_ticketing_app/todaycollection.html', {'total_amount':total_amount, 'today_date':today_date})

def overallcollection(request):
    overall_amount = BookedTicketDetails.objects.all().values('Route_No','Booked_Date__month','Booked_Date__year').annotate(totalamt=Sum('Total_Amount'))
    return render(request, 'mtc_bus_ticketing_app/overallcollection.html',{'overall_amount':overall_amount})

# Passenger Site

def routesearch(request):
    form1 = RouteSerchForm()
    form2 = RouteNoSearchForm()
    if request.method == 'POST':
        form1 = RouteSerchForm(request.POST)
        form2 = RouteNoSearchForm(request.POST)
        if form1.is_valid():
            From = form1.cleaned_data['From']
            To = form1.cleaned_data['To']
            busroutedetails = BusRouteDetails.objects.filter(From=From,To=To)
            if busroutedetails.exists():
                return render(request, 'mtc_bus_ticketing_app/busdetails.html', {'busroutedetails':busroutedetails})
            else:
                messages.error(request, 'No results found')
        else:
            if form2.is_valid():
                BusRoute = form2.cleaned_data['BusRoute']
                busroutedetails = BusRouteDetails.objects.filter(BusRoute=BusRoute)
                if busroutedetails.exists():
                    return render(request, 'mtc_bus_ticketing_app/busdetails.html', {'busroutedetails':busroutedetails})
                else:
                    messages.error(request, 'No results found')
    return render(request, 'mtc_bus_ticketing_app/routesearch.html', {'form1':form1,'form2':form2})

def busdetails(request):
    busroutedetails = request.GET.getlist('busroutedetails')
    return render(request, 'mtc_bus_ticketing_app/busdetails.html', {'busroutedetails':busroutedetails})

def busdetails_bookticket(request,id):
    data = BusRouteDetails.objects.get(id=id)
    form = BookedTicketDetailsForm(initial={
            'Route_No': data.BusRoute,
            'From_location': data.From,
            'To_location': data.To,
            'Ticket_Amount': data.TicketAmount,
        })
    if request.method == 'POST':
        checkbox1 = 'checkbox1' in request.POST
        checkbox2 = 'checkbox2' in request.POST
        checkbox3 = 'checkbox3' in request.POST
        form = BookedTicketDetailsForm(request.POST)
        if form.is_valid():
            booked_ticket = BookedTicketDetails(
                Route_No = form.cleaned_data['Route_No'],
                From_location = form.cleaned_data['From_location'],
                To_location = form.cleaned_data['To_location'],
                Ticket_Amount = form.cleaned_data['Ticket_Amount'],                
                No_of_Tickets = form.cleaned_data['No_of_Tickets'],
                Total_Amount = form.cleaned_data['Total_Amount'],
                Booked_Date = datetime.now(),
                Expired_Date = datetime.now() + timedelta(minutes=data.Duration_in_Minutes) + timedelta(minutes=10),
            )
            if checkbox1 == checkbox1 or checkbox2 == checkbox2 or checkbox3 == checkbox3:
                booked_ticket.save()
                request.session['latest_ticket_id'] = booked_ticket.id
                return redirect('/mtc_bus_ticketing_app/ticketdetails')
    return render(request, 'mtc_bus_ticketing_app/ticketbookingform.html', {'data':data,'form':form})

def ticketdetails(request):
    latest_ticket_id = request.session.get('latest_ticket_id')
    latest_ticket = None
    if latest_ticket_id:
        try:
            latest_ticket = BookedTicketDetails.objects.get(id=latest_ticket_id)
        except BookedTicketDetails.DoesNotExist:
            pass
    return render(request, 'mtc_bus_ticketing_app/ticketdetails.html', {'latest_ticket':latest_ticket})

def ticketdetails_download_as_pdf(request):
    pass