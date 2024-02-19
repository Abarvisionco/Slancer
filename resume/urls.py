from django.urls import path
from resume import views

urlpatterns = [
    path('',views.resume_home, name='resume_home'),
    path('create/',views.create_resume, name='resume_create')
]