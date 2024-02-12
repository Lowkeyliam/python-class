courses = ["MIT", "Cyber security", "Data science"]
print(courses)

# Accessing an element in an array
print(courses[1])

# Looping through an array
for course in courses:
    print(course)

# Adding a new element into an array
courses.append("Android programming")
print(courses)

# Deleting an element from an array
courses.remove("Data science")
print(courses)