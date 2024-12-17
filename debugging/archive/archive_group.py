import numpy as np
import random

def student_data():
    grade_column = "Grade"
    participation_column = "participation"
    peer_review_column = "Peer_review"


    students_dic = {}
    simulated_students_n = 11
    
    base_grade = 60
    base_participation = 40
    base_peer_review = 50
    
    randomness_rate = 50 / 100
    base_grade_range = base_grade * randomness_rate
    base_participation_range = base_participation * randomness_rate
    base_peer_review_range= base_peer_review * randomness_rate
    
    collected_student_1 = {grade_column: base_grade, 
                           participation_column: 40,
                           peer_review_column: 50}
                           
    students_dic["Student_1"] = collected_student_1
  
    
    for current_index in range(2, simulated_students_n):
        current_student = "Student_" + str(current_index)
        
        random_grade_adjustment = random.randint(-base_grade_range, base_grade_range)
        random_participation_adjustment = random.randint(-base_participation_range, base_participation_range)
        random_peer_review_adjustment = random.randint(-base_peer_review_range, base_peer_review_range)
        
        
        students_dic[current_student] = {grade_column: base_grade + random_grade_adjustment, participation_column: base_participation + random_participation_adjustment, peer_review_column: base_peer_review + random_peer_review_adjustment }
    
    # Generating other students' data
    # generated_student_2 = {"Grade": collected_student_1["Grade"] + 20,
                           # "participation": collected_student_1["participation"] + 50,
                           # "Peer_review": collected_student_1["Peer_review"] + 45}
    # generated_student_3 = {"Grade": collected_student_1["Grade"] + 15,
                           # "participation": collected_student_1["participation"] + 40,
                           # "Peer_review": collected_student_1["Peer_review"] + 35}
    # generated_student_4 = {"Grade": collected_student_1["Grade"] - 5,
                           # "participation": collected_student_1["participation"],
                           # "Peer_review": collected_student_1["Peer_review"] - 10}
    # generated_student_5 = {"Grade": collected_student_1["Grade"] + 13,
                           # "participation": collected_student_1["participation"] + 35,
                           # "Peer_review": collected_student_1["Peer_review"] + 25}
    # generated_student_6 = {"Grade": collected_student_1["Grade"] + 5,
                           # "participation": collected_student_1["participation"],
                           # "Peer_review": collected_student_1["Peer_review"]}
    # generated_student_7 = {"Grade": collected_student_1["Grade"] + 5,
                           # "participation": collected_student_1["participation"] + 5,
                           # "Peer_review": collected_student_1["Peer_review"] + 5}
    # generated_student_8 = {"Grade": collected_student_1["Grade"] - 5,
                           # "participation": collected_student_1["participation"] - 5,
                           # "Peer_review": collected_student_1["Peer_review"] - 5}
    # generated_student_9 = {"Grade": collected_student_1["Grade"] + 30,
                           # "participation": collected_student_1["participation"] + 55,
                           # "Peer_review": collected_student_1["Peer_review"] + 47}
    # generated_student_10 = {"Grade": collected_student_1["Grade"] + 1,
                            # "participation": collected_student_1["participation"] + 1,
                            # "Peer_review": collected_student_1["Peer_review"] + 1}
    # generated_student_11 = {"Grade": collected_student_1["Grade"] - 1,
                            # "participation": collected_student_1["participation"] - 1,
                            # "Peer_review": collected_student_1["Peer_review"] - 1}
    
    # Store all students' data in a list
    # students = [
        # collected_student_1,
        # generated_student_2,
        # generated_student_3,
        # generated_student_4,
        # generated_student_5,
        # generated_student_6,
        # generated_student_7,
        # generated_student_8,
        # generated_student_9,
        # generated_student_10,
        # generated_student_11
    # ]
    
    return students_dic

def min_max_normalization(data_to_normalize):
    """
    Performs Min-Max normalization on the input variable.

    Parameters:
        data_to_normalize (list): The input data to be normalized.

    Returns:
        numpy array: The normalized data.
    """
    data = np.array(data_to_normalize, dtype=float)
    min_value = np.min(data)
    max_value = np.max(data)
    
    normalized_data = (data - min_value) / (max_value - min_value)
    
    return normalized_data

def main():
    # Get the list of students
    students = student_data()

    # Extract data for normalization
    grades = [student["Grade"] for student in students]
    participation = [student["participation"] for student in students]
    peer_review = [student["Peer_review"] for student in students]

    # Normalize each criteria
    normalized_grades = min_max_normalization(grades)
    normalized_participation = min_max_normalization(participation)
    normalized_peer_review = min_max_normalization(peer_review)


    # inputs
    grade_weight = 0.5
    participation_weight = 0.3
    peer_review_weight = 0.2

    # Calculate the final score for each student
    final_scores = []
    for values in range(len(students)):
        score = (normalized_grades[values] * grade_weight +
                 normalized_participation[values] * participation_weight +
                 normalized_peer_review[values] * peer_review_weight)
        final_scores.append(score)

    # Output the final scores
    for value, score in enumerate(final_scores):
        print(f"Student {value+1} - Final Score: {score:.2f}")

    # Define the weights for each criterion
def adjust_weights(grade_weight, participation_weight, peer_review_weight):
    total = grade_weight + participation_weight + peer_review_weight

    if total > 1:
    # so total equals 1
        grade_weight = grade_weight / total
        participation_weight = participation_weight / total
        peer_review_weight = peer_review_weight / total
    
    return grade_weight, participation_weight, peer_review_weight


#main()
