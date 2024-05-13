from django.urls import path
from company import views


urlpatterns = [
    path('', views.company, name='company'),
    path('<int:id>/',views.company_detail, name='co_detail'),
    path('add-company/<int:company_id>/', views.add_resume_to_company, name='add_co'),
    path('resume/', views.company_resume, name='company_resume'),
    path('all/', views.filter_all_co, name='co_all')
]