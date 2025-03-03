# Step 1: Create the dictionary
student_profile = {
    'names': ['John', 'Alice', 'Bob', 'Alice', 'John'],
    'grades': [85, 90, 78, 92, 88]
}

# Step 2: Print all different values present in key 1 (names)
unique_names = set(student_profile['names'])
print("Unique names:", unique_names)

# Step 3: Print all values present in key 2 (grades)
print("Grades:", student_profile['grades'])

# Step 4: Print a message
message = f"The student profile contains {len(unique_names)} unique names and the grades for each student."
print(message)
