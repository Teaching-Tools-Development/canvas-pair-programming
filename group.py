import numpy as np

def student_data():
    collected_student_1 = {"Grade": 60, 
                           "participation": 40,
                           "Peer_review": 50}
    
    # Generating other students' data
    generated_student_2 = {"Grade": collected_student_1["Grade"] + 20,
                           "participation": collected_student_1["participation"] + 50,
                           "Peer_review": collected_student_1["Peer_review"] + 45}
    generated_student_3 = {"Grade": collected_student_1["Grade"] + 15,
                           "participation": collected_student_1["participation"] + 40,
                           "Peer_review": collected_student_1["Peer_review"] + 35}
    generated_student_4 = {"Grade": collected_student_1["Grade"] - 5,
                           "participation": collected_student_1["participation"],
                           "Peer_review": collected_student_1["Peer_review"] - 10}
    generated_student_5 = {"Grade": collected_student_1["Grade"] + 13,
                           "participation": collected_student_1["participation"] + 35,
                           "Peer_review": collected_student_1["Peer_review"] + 25}
    generated_student_6 = {"Grade": collected_student_1["Grade"] + 5,
                           "participation": collected_student_1["participation"],
                           "Peer_review": collected_student_1["Peer_review"]}
    generated_student_7 = {"Grade": collected_student_1["Grade"] + 5,
                           "participation": collected_student_1["participation"] + 5,
                           "Peer_review": collected_student_1["Peer_review"] + 5}
    generated_student_8 = {"Grade": collected_student_1["Grade"] - 5,
                           "participation": collected_student_1["participation"] - 5,
                           "Peer_review": collected_student_1["Peer_review"] - 5}
    generated_student_9 = {"Grade": collected_student_1["Grade"] + 30,
                           "participation": collected_student_1["participation"] + 55,
                           "Peer_review": collected_student_1["Peer_review"] + 47}
    generated_student_10 = {"Grade": collected_student_1["Grade"] + 1,
                            "participation": collected_student_1["participation"] + 1,
                            "Peer_review": collected_student_1["Peer_review"] + 1}
    generated_student_11 = {"Grade": collected_student_1["Grade"] - 1,
                            "participation": collected_student_1["participation"] - 1,
                            "Peer_review": collected_student_1["Peer_review"] - 1}
    
    # Store all students' data in a list
    students = [
        collected_student_1,
        generated_student_2,
        generated_student_3,
        generated_student_4,
        generated_student_5,
        generated_student_6,
        generated_student_7,
        generated_student_8,
        generated_student_9,
        generated_student_10,
        generated_student_11
    ]
    
    return students

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
    # Step 1: Get the list of students
    students = student_data()

    # Step 2: Extract data for normalization
    grades = [student["Grade"] for student in students]
    participation = [student["participation"] for student in students]
    peer_review = [student["Peer_review"] for student in students]

    # Step 3: Normalize each criterion
    normalized_grades = min_max_normalization(grades)
    normalized_participation = min_max_normalization(participation)
    normalized_peer_review = min_max_normalization(peer_review)

    # Step 4: Define the weights for each criterion
    grade_weight = 0.5
    participation_weight = 0.3
    peer_review_weight = 0.2

    # Step 5: Calculate the final score for each student
    final_scores = []
    for values in range(len(students)):
        score = (normalized_grades[values] * grade_weight +
                 normalized_participation[values] * participation_weight +
                 normalized_peer_review[values] * peer_review_weight)
        final_scores.append(score)

    # Output the final scores
    for value, score in enumerate(final_scores):
        print(f"Student {value+1} - Final Score: {score:.2f}")

main()
