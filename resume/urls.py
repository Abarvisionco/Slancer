from django.urls import path
from resume import views


urlpatterns = [
    path('',views.resume_home, name='resume_home'),
    path('skills/',views.skills,name='resume_skills'),
    path('skills/add/',views.add_skill,name='resume_skills_add'),
    path('skills/<int:id>/', views.update_skill, name='resume_skills_update'),
    path('skills/<int:id>/delete/',views.delete_skill,name='resume_skills_delete')
]