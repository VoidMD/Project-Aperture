import re
import django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import SignUpForm, TicketForm

def home(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        page = 'login'
        if request.method == 'POST':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username = username)
            except:
                messages.error(request, 'User dose not exist')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username OR password does not exist')
        context={'page' : page}
        return render(request, 'login.html', context)
        

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User has been created')
            messages.success(request, 'Welcome '+user.username)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong !')

    return render(request,'login.html', {'form':form})

def userProfile(request):
    if request.user.is_authenticated:
        user = request.user
        form_password=PasswordChangeForm(user)
        if request.method == 'POST':
            form = PasswordChangeForm(user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password has been changed')
                return redirect('profile')
            else:
                messages.error(request, 'Something went wrong! Please try again')

        context = {'passForm':form_password}
        return render(request, 'profile.html', context)
    else:
        return redirect('login')

def flight_search(request):
    form = TicketForm()
    if request.method == 'POST':
        counfrom = request.POST.get('country-from')
        counto = request.POST.get('country-to')
        datefrom = request.POST.get('date-from')
        dateto = request.POST.get('date-to')

        if datefrom == "":
            messages.error(request, 'Please enter correct information')
            redirect('flight_search')
        else:
            flights = Flight.objects.filter(Date= datefrom, Source_City= counfrom , Destination_City = counto)
            form = TicketForm()
            
            return render(request,'Flights.html',{'flights':flights,'form':form})
        
    return render(request,'Flight_Search.html')


def manage_booking(request):
    try:
        tkts = Ticket.objects.get(User = request.user)
        flight = Flight.objects.get(id = tkts.Flight_Number.id)
        return render(request,'manage_flights.html',{'flight':flight,'tkt':tkts})
    except:
        messages.error(request, 'There are no bookings')
        return redirect('home')

def check_in(request):
    try:
        tkts = Ticket.objects.get(User = request.user)
        flight = Flight.objects.get(id = tkts.Flight_Number.id)
        return render(request,'check_in.html',{'flight':flight,'tkt':tkts})
    except:
        messages.error(request, 'There are no bookings')
        return redirect('home')