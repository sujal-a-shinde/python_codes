student = {
    "name": "Sujal",
    "age": 22,
    "Gender": "Male",
    "city": "Pune",
}

print("age" in student)
print(22 in student)  # only check Key no value

k = input("Enter key : ")
if k in student:
    print(student[k])
else:
    print("Key Does not exist")
