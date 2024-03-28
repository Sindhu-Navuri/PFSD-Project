import random
import string

from .forms import IntegerDateForm, PieChartForm
import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello1(request):
    return HttpResponse("<center>Welcome to MNC Homepage</center>")

def NewHomepage(request):
    return render(request,'NewHomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'print_to_console.html',a1)

def randomcall(request):
    return render(request,'randomOTPgenerator.html')

def randomlogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1=''.join(random.sample(string.digits,k=a2))
    a1={'ran1':ran1}
    return render(request,'randomOTPgenerator.html',a1)

def getdate(request):
    return render(request,'DateTime.html')

from django.shortcuts import render
def DateTime(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'DateTime.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'DateTime.html',{'form':form})

def getRegister(request):
    return render(request,'RegisterPage.html')

from .models import *
from django.shortcuts import render,redirect
def Sindhuloginfunction(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Sindhu.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a differenet email")
        Sindhu.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('NewHomepage')
    return render(request,'RegisterPage.html')


def getPieChart(request):
    return render(request,'PieChart.html')

import matplotlib.pyplot as plt
import numpy as np
def PieChart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'PieChart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'PieChart.html', {'form': form})


def getCar(request):
    return render(request,'Car.html')


import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '00cca2a289db22b037af91f404dda286'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


def Feedbackcall(request):
    return render(request,'myfeedbackform.html')

def Feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        suggestion = request.POST.get('suggestion')
        if contactus.objects.filter(email=email).exists():
            return HttpResponse("Feedback already submitted.")
        contactus.objects.create(name=name,email=email,suggestion=suggestion)
        return redirect('NewHomepage')
    return render(request,'myfeedbackform.html')

from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return  render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'NewHomepage.html')