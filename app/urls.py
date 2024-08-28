from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assignment/', views.assignment, name='assignment'),
    path("canvas-users/", views.get_canvas_users, name="get_canvas_users"),
    path('test-student-grades/', views.get_test_student_grades, name='test_student_grades'),
]
