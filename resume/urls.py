from django.urls import path
from resume import views, courses_views
from resume import exam_works_views, work_views, courses_views, skills_views

urlpatterns = [
    path('',views.resume_home, name='resume_home'),
    path("<int:id>/",views.resume,name="resume"),
    # skills CRUD
    path('skills/',skills_views.skills,name='resume_skills'),
    path('skills/add/',skills_views.add_skill,name='resume_skills_add'),
    path('skills/<int:id>/', skills_views.update_skill, name='resume_skills_update'),
    path('skills/<int:id>/delete/',skills_views.delete_skill,name='resume_skills_delete'),
    # exam CRUD
    path('examـworks/',exam_works_views.home,name='exam'),
    path('exam_works/add/', exam_works_views.add_exam, name='exam_add'),
    path('exam_works/<int:id>/', exam_works_views.update_exam, name='exam_edit'),
    path('examـworks/<int:id>/delete/',exam_works_views.delete_exam, name='exam_delete'),
    # work CRUD
    path('work_experience/', work_views.home, name='work_experience'),
    path('work_experience/add/',work_views.add_work, name='work_add'),
    path('work_experience/<int:id>/', work_views.update_work, name='work_update'),
    path('work_experience/<int:id>/delete/',work_views.delete_work, name='work_delete'),
    # courses CRUD
    path('course/',courses_views.home, name='courses'),
    path('course/add/',courses_views.add_course,name='course_add'),
    path('course/<int:id>/',courses_views.update_course,name='course_update'),
    path('course/<int:id>/delete/',courses_views.delete_course, name='course_delete')
]