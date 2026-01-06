from django.urls import path
from . import views  # Import views from the 'Base' app

urlpatterns = [
    path('', views.contact, name='contact'),  
]
