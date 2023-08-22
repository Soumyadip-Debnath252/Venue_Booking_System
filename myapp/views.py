from django.utils.dateparse import parse_date
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from . forms import MyUserRegFrm,MyLoginFrm,  BookingForm
from .models import Book, Venue

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')  

def RegLog(request):
    return render(request, 'myapp/Services.html')  

def Register(request):
    if request.method == "POST":
        form = MyUserRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Your registration is successfull')
            except Exception as e:
                messages.error(request,'Your registration is unsuccessfull')
    else:
        form=MyUserRegFrm()
    return render(request, 'myapp/register.html', {'form':form}) 

def userLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/catalouge')
    else:
        if request.method == "POST":
            form = MyLoginFrm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/catalouge')
        else:
            form= MyLoginFrm()
        return render(request, 'myapp/Login.html', {'form':form})

def usrLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def catalouge(request):
    gallery=Venue.objects.all()
    return render(request, 'myapp/gallery.html',{'gallery':gallery})

def book(request,vid):
    if request.user.is_authenticated:
        venue=Venue.objects.get(vid=vid)
        if request.POST:
            form=BookingForm(request.POST)
            edate=request.POST.get('eventdate')
            if form.is_valid():
                try:
                    instance=form.save(False)
                    c1=Q(venue_id=vid)
                    c2=Q(eventdate= parse_date(edate))
                    book=Book.objects.filter( c1 & c2 )
                    if book:
                        messages.error(request, 'Venue is already booked')
                    else:
                        instance.user_id=request.user.id
                        instance.venue_id=vid
                        instance.charges=venue.vcharges
                        instance.save()
                        messages.success(request, 'Booking has been completed')
                        form = BookingForm()
                except Exception as e:
                    messages.error(request, e)
        else:
            form=BookingForm()
        return render(request, 'myapp/book.html', {'gallery':venue, 'form':form})
    else:
        return HttpResponseRedirect('/login')

def bookingDetails(request):
    if request.user.is_authenticated:
        allBook=Book.objects.raw("SELECT b.*, v.vname FROM myapp_book b INNER JOIN myapp_venue v ON b.venue_id=v.vid WHERE b.user_id={} ORDER BY b.eventdate DESC".format(request.user.id))
        return render(request, 'myapp/bookDetails.html', {'allBook':allBook})
    else:
        return HttpResponseRedirect('/login')