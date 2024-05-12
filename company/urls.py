from django.urls import path
from company import views


urlpatterns = [
    path('', views.company, name='company'),
    path('<int:id>/',views.company_detail, name='co_detail'),
    path('add-company/<int:company_id>/', views.add_resume_to_company, name='add_co')
]