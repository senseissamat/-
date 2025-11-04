students_data = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 78)
]

def read_students(data):
    students = []
    scores = []

    for name, grade in data:
        students.append((name, grade))
        scores.append(grade)

    print("Student List:")
    for name, grade in students:
        print(f"{name} - {grade}")

    if scores:
        average = sum(scores) / len(scores)
        print(f"\nAverage Score: {average:.2f}")
    else:
        print("No data available to calculate average.")

print("========== TASK 1 ==========")
read_students(students_data)


students = [
    "Aigerim, 89",
    "Nurlan, 74",
    "Aliya, 95"
]

print("\n========== TASK 2 ==========")
name = input("Enter student name: ")
grade = input("Enter student grade: ")

students.append(f"{name}, {grade}")

print("\nRecord added successfully!")
print("\nUpdated list:")
for s in students:
    print(s)

data = ["Alice", "Bob", "Charlie"]
print("\n========== TASK 3 ==========")
print("File read successfully.")

grade_input = input("Enter a grade (number): ")
try:
    grade = float(grade_input)
    print(f"You entered grade: {grade}")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

print("Program completed.")

class LowScoreError(Exception):
    pass

print("\n========== TASK 4 ==========")
try:
    grade_input = input("Enter grade: ")
    grade = int(grade_input)
    if grade < 50:
        raise LowScoreError("Score too low! Student failed.")
    print("Grade accepted.")
except ValueError:
    print("Error: Please enter a valid integer.")
except LowScoreError as e:
    print("Custom Exception:", e)
finally:
    print("Program completed.")
