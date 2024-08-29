
import os
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def assignment(request):
    course_id = '25655'  # Replace with your actual course ID
    base_url = f'https://canvas.nau.edu/api/v1/courses/{course_id}'
    headers = {
        "Authorization": f"Bearer {settings.CANVAS_API_TOKEN}"
    }

    # Step 1: Get all assignments
    assignments_url = f'{base_url}/assignments'
    assignments_response = requests.get(assignments_url, headers=headers)

    try:
        assignments_response.raise_for_status()
        assignments = assignments_response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'message': f'Request error: {e}'})

    # Step 2: Get all enrollments (students)
    enrollments_url = f'{base_url}/enrollments'
    enrollments_response = requests.get(enrollments_url, headers=headers)

    try:
        enrollments_response.raise_for_status()
        enrollments = enrollments_response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'message': f'Request error: {e}'})

    student_grades = []

    # Step 3: Loop through each student and each assignment to get grades
    for enrollment in enrollments:
        # Filter for students only
        if enrollment.get('role') == 'StudentEnrollment':
            student_name = enrollment.get('user', {}).get('name', 'Unknown')
            total_grade = 0
            total_possible_points = 0
            
            for assignment in assignments:
                assignment_id = assignment.get('id')
                points_possible = assignment.get('points_possible', 0)
                
                if not assignment_id or points_possible == 0:
                    continue
                
                # Get submission for the current student for the current assignment
                submission_url = f'{base_url}/assignments/{assignment_id}/submissions/{enrollment["user_id"]}'
                submission_response = requests.get(submission_url, headers=headers)
                
                try:
                    submission_response.raise_for_status()
                    submission = submission_response.json()
                    grade = submission.get('score', 0)  # Get the score (0 if not submitted)
                    total_grade += grade
                    total_possible_points += points_possible
                except requests.exceptions.RequestException:
                    continue
            
            # Calculate the percentage grade
            if total_possible_points > 0:
                percentage_grade = (total_grade / total_possible_points) * 100
            else:
                percentage_grade = 0
            
            student_grades.append({
                'student_name': student_name,
                'total_grade': percentage_grade
            })

    return render(request, 'assignment.html', {'students': student_grades})

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
    course_id = '25655'  # Replace with your actual course ID
    base_url = f'https://canvas.nau.edu/api/v1/courses/{course_id}'
    headers = {
        "Authorization": f"Bearer {settings.CANVAS_API_TOKEN}"
    }

    # Step 1: Get all assignments
    assignments_url = f'{base_url}/assignments'
    assignments_response = requests.get(assignments_url, headers=headers)
    
    try:
        assignments_response.raise_for_status()
        assignments = assignments_response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'message': f'Request error: {e}'})
    
    # Step 2: Get all enrollments (students)
    enrollments_url = f'{base_url}/enrollments'
    enrollments_response = requests.get(enrollments_url, headers=headers)
    
    try:
        enrollments_response.raise_for_status()
        students = enrollments_response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'message': f'Request error: {e}'})
    
    student_grades = []
    
    # Step 3: Loop through each student and each assignment to get grades
    for student in students:
        student_name = student.get('user', {}).get('name', 'Unknown')
        total_grade = 0
        
        for assignment in assignments:
            assignment_id = assignment.get('id')
            
            if not assignment_id:
                continue
            
            # Get submission for the current student for the current assignment
            submission_url = f'{base_url}/assignments/{assignment_id}/submissions/{student["user_id"]}'
            submission_response = requests.get(submission_url, headers=headers)
            
            try:
                submission_response.raise_for_status()
                submission = submission_response.json()
                grade = submission.get('score', 0)  # Get the score (0 if not submitted)
                total_grade += grade
            except requests.exceptions.RequestException:
                continue
        
        student_grades.append({
            'student_name': student_name,
            'total_grade': total_grade
        })
    
    return render(request, 'student_grades.html', {'students': student_grades})