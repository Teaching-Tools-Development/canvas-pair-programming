from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/test-student-grades/', views.get_test_student_grades, name='test_student_grades'),
]
