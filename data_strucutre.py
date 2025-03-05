# Creating the student_profile dictionary
student_profile = {
    "names": ["Alice", "Bob", "Cathy", "David"],
    "grades": [85, 90, 88, 92]
}

# Data extraction and display
# 1. Print all different values present in key 1 (names)
print("Student Names:")
for name in student_profile["names"]:
    print(name)

# 2. Print all values present in key 2 (grades)
print("\nStudent Grades:")
for grade in student_profile["grades"]:
    print(grade)

# 3. Print a message for each student
print("\nStudent Information:")
for i in range(len(student_profile["names"])):
    print(f"Student {student_profile['names'][i]} obtained {student_profile['grades'][i]}% in BSE.")
