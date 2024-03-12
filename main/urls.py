from django.urls import path
from main import views

urlpatterns = [
    # index page
    path('', views.home, name='home'),
]