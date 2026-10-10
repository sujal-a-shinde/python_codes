student = {"name": "Sujal", "age": 21}

# Update
student["age"] = 22
print(student)

# Add (same syntax but it does not exist in dictionary then it will add)
student["Gender"] = "Male"
print(student)

# Add.... by methods
student.update(
    {
        "city": "Pune",
        "Phone No": 2394740942,
        "State": "Maharashtra",
    }
)
print(student)
