from django.shortcuts import render
import os
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'base.html')
def get_test_student_grades(request, course_id):
    # Configure Canvas API
    API_URL = 'https://canvas.nau.edu'
    API_TOKEN = '19664~Tn6ehcVae9mKmYr8nKyCxJtZa2ameWDFJnf8URhCwrznzTEZD9C73hxeY7CxMGHC'  # Replace with your actual Canvas API token

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    # Endpoint to get enrollments
    endpoint = f'{API_URL}/courses/{course_id}/enrollments'
    
    # Parameters to specify the type of enrollment (student) and include grades
    params = {
        'type': 'StudentEnrollment',
        'include[]': 'grades'
    }
    
    # Make the request to the Canvas API
    response = requests.get(endpoint, headers=headers, params=params)
    enrollments = response.json()
    
    # Filter the enrollments to find the Test Student
    test_student_data = None
    for enrollment in enrollments:
        if enrollment.get('user', {}).get('name') == 'Test Student':
            test_student_data = enrollment
            break
    
    # Render the data to a template
    context = {
        'test_student_data': test_student_data
    }
    return render(request, 'test_student_grades.html', context)
# test