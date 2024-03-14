from django.urls import path
from resume import views
from resume import exam_works_views


urlpatterns = [
    path('',views.resume_home, name='resume_home'),
    path('skills/',views.skills,name='resume_skills'),
    path('skills/add/',views.add_skill,name='resume_skills_add'),
    path('skills/<int:id>/', views.update_skill, name='resume_skills_update'),
    path('skills/<int:id>/delete/',views.delete_skill,name='resume_skills_delete'),
    path('exam-works/',exam_works_views.home,name='exam'),
    path('exam_works/add/', exam_works_views.add_exam, name='exam_add'),
    path('exam_works/<int:id>/', exam_works_views.update_exam, name='exam_edit'),
    path('exam-works/<int:id>/delete/',exam_works_views.delete_exam, name='exam_delete'),
]