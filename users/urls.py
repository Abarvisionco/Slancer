from django.urls import path
from users import views






urlpatterns = [
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login'),
    path('verify/',views.verify,name='verify'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('profile_views/',views.profile_views,name='profile_views'),
]