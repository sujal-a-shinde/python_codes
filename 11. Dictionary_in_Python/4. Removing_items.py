student = {
    "name": "Sujal",
    "age": 22,
    "Gender": "Male",
    "city": "Pune",
}

student.pop("name")
print(student)

student.clear()
print(student)

del student["age"]
print(student)
