students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {
        "name": "Karan",
        "age": 22,
        "city": "Pune",
        "details": {"ph": 909309, "gender": "Male"},
    },
}

# How to Access the data from Dict in Dict
print(students["101"])
print(students["101"]["name"])
print(students["103"]["city"])
print(students["103"]["details"]["gender"])


# Iteration

total = 0
for roll_no, details in students.items():
    # print(f"Roll No : {roll_no}, Details : {details}")
    total += details["age"]
    print(f"Roll No : {roll_no}, Names : {details['name']} and Age : {details['age']}")

print(total)



