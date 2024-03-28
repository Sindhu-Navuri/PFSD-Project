from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',NewHomepage,name='NewHomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate/',getdate,name='getdate'),
    path('DateTime/',DateTime,name='DateTime'),
    path('getRegister/',getRegister,name='getRegister'),
    path('Sindhuloginfunction/',Sindhuloginfunction,name='Sindhuloginfunction'),
    path('getPieChart/', getPieChart, name='getPieChart'),
    path('PieChart/', PieChart, name='PieChart'),
    path('getCar/', getCar, name='getCar'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('Feedbackcall/',Feedbackcall,name='Feedbackcall'),
    path('Feedback/',Feedback,name='Feedback'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('signup/',signup,name='signup'),
]