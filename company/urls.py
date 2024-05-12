from django.urls import path
from company import views


urlpatterns = [
    path('', views.company, name='company'),
    path('<int:id>/',views.company_detail, name='co_detail')
]