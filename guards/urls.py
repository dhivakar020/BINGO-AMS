from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='guards/registration/login.html'), name='login'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance-success/', views.attendance_success,
         name='attendance_success'),
    path('attendance-report/', views.view_attendance_report,
         name='attendance_report'),
]
