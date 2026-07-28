# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================


def add_student(students):
    """Prompts for a student's name, ID, and scores, then adds the record."""
    name = input("Student name: ")
    id_input = input("Student ID: ")

    if not id_input.isdigit():
        print("Error: Student ID must be a number.")
        return

    student_id = int(id_input)

    # Check for duplicate ID
    for student in students:
        if student["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return

    num_scores_input = input("How many scores? ")
    if not num_scores_input.isdigit() or int(num_scores_input) <= 0:
        print("Error: Number of scores must be a positive integer.")
        return

    num_scores = int(num_scores_input)
    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Returns the average of a list of scores, rounded to 2 decimal places."""
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def display_all_students(students):
    """Prints a formatted table of all students: name, ID, scores, average."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 60)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<20}{'Average':<10}")
    print("-" * 60)

    for student in students:
        scores_str = ", ".join(format_score(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<20}{average:<10}")

    print("-" * 60)


def format_score(score):
    """Formats a score without a trailing .0 for whole numbers."""
    return f"{score:g}"


def find_student_by_id(students, student_id):
    """Returns the student dict matching the given ID, or None if not found."""
    for student in