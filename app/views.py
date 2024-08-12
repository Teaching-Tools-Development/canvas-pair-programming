
import os
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_canvas_users(request):
    # Get the API token from the environment variable

    canvas_instance = "https://canvas.nau.edu"
    course_id = "25655"

    url = f"{canvas_instance}/api/v1/courses/{course_id}/users"
    headers = {
        "Authorization": f"Bearer {settings.CANVAS_API_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        return render(request, 'users.html', {'users': users})
    else:
        return JsonResponse({"error": f"Failed to get users: {response.status_code}"}, status=response.status_code)

def get_test_student_grades(request):
    course_id = 25655
    api_url = f'https://canvas.nau.edu/api/v1/courses/{course_id}/students/submissions'
    headers = {
        'Authorization': 'Bearer 19664~4UrrEFtMzTy7fwcvT8EJTu3vfnvAJtF7RcxVWhtvrvn8uNUnHQCeXUFxTmwm6ZJv'
    }
    params = {
        'include[]': ['submission', 'rubric_assessment', 'user', 'assignment']
    }

    response = requests.get(api_url, headers=headers, params=params)

    try:
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Ensure response data is in JSON format
        response_data = response.json()

        # Parse the response data to extract relevant information
        grades = []
        for submission in response_data:
            student_name = submission['user']['name']
            assignment_name = submission['assignment']['name']
            grade = submission['grade']
            grades.append({
                'student_name': student_name,
                'assignment_name': assignment_name,
                'grade': grade
            })

        return render(request, 'test_student_grades.html', {'grades': grades})
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'error': f'HTTP error occurred: {http_err}'}, status=response.status_code)
    except requests.exceptions.RequestException as req_err:
        return JsonResponse({'error': f'Request error occurred: {req_err}'}, status=500)
    except ValueError as json_err:
        return JsonResponse({'error': f'JSON decode error: {json_err}', 'response_content': response.text}, status=500)