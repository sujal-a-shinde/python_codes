# union()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Using the | operator
print(a | b)  # {1, 2, 3, 4, 5, 6}
# Using the union() method
print(a.union(b))  # {1, 2, 3, 4, 5, 6}


# intersection()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Using the & operator
print(a & b)  # {3, 4}
# Using the intersection() method
print(a.intersection(b))  # {3, 4}

# Real-world Application: Student Records

math_students = {"Rahul", "Priya", "Karan", "Sana"}
science_students = {"Priya", "Karan", "Aman"}
print("Students in BOTH Math and Science:")
print(math_students & science_students)
# Output: {'Priya', 'Karan'}

print("\nStudents in EITHER Math OR Science:")
print(math_students | science_students)
# Output: {'Rahul', 'Priya', 'Karan', 'Sana', 'Aman'}
