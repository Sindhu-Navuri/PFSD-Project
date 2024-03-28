from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('sendemails/', views.sendemails, name='sendemails'),  # This maps the view to the URL
]
