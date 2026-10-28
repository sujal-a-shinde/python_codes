"""
Q1.Create a dictionary for a student, including keys like
   city, and marks (as a list of scores). Print each piece of
   information using its key.
"""

student = {
    "name": "Sujal",
    "city": "Pune",
    "Marks": [76, 87, 98, 56, 78],
}

print(f"Name : {student["name"]}\nCity : {student["city"]}\nMarks : {student["Marks"]}")

"""
Q2.Define a dictionary with five subjects and their respective marks. 
   Utilize the get() method to try accessing a subject that is not in the 
   dictionary, ensuring it prints "Not Available" as a default
"""
marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}

sub1 = input("Enter Subject : ")
sub = marks.get(sub1, "Not Available")
print(f"{sub1} : {sub}")


"""
Q3.Construct a dictionary containing four product names and their 
   prices. Prompt the user to enter a product name. Use the in 
   keyword to check if it exists; if so, display its price. Otherwise, 
   inform the user "Product not found.
"""
product = {
    "RC Car": 2500,
    "Bottle": 800,
    "Teddy_Bear": 300,
    "Bag": 400,
    "Mobile_phone": 44_000,
}

# 1st Method
is_product = input("Enter Product Name : ")
price = product.get(is_product, "Product Not Found")
print(price)

# 2nd Method
is_product = input("Enter Product Name : ")
if is_product in product:
    print(f"Product : {is_product} and Price : {product[is_product]}")
else:
    print("Product not found")


"""
Q4.Create a dictionary mapping five countries to their capital cities. Iterate 
   through this dictionary using the 
   the format: Country →Capital.
"""
mapping = {
    "India": "Delhi",
    "China": "Beijing",
    "Germany": "Berlin",
    "England": "Londan",
    "Ireland": "Dublin",
}

print("countries capitals")
for country, capital in mapping.items():
    print(f"{country}     {capital} ")


"""
Q5.Given a dictionary of marks for different subjects, loop over its 
   values() to calculate and print the total marks and the average mark obtained.
"""
marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}

# 1st method
n = len(marks)
total = 0
for mark in marks.values():
    total += mark
    average = total / n
print(f"The Total Marks : {total} and average : {average}")

# 2nd method
n = len(marks)
total = sum(marks.values())
average = total / n

print(f"The Total Marks : {total} and average : {average}")


"""
Q6.Populate a dictionary with six student names and their corresponding 
   marks. Loop through it and print the names of all students who achieved 
   a score above 75.
"""
student = {
    "sujal": 99,
    "anuj": 28,
    "zaid": 56,
    "sayali": 43,
    "manish": 71,
}

for stud, marks in student.items():
    if marks <= 75:
        print(f"Student : {stud} and Marks : {marks}")


"""
Q7.Write a Python function named 
   dictionaries (merge_dicts(d1, d2) that accepts two d1 and d2) as 
   arguments and returns a new dictionary formed by merging them using the 
   update() method. Ensure d1 remains unchanged.
"""


def merge_dicts(d1, d2):
    new_dict = {}
    new_dict.update(d1)
    new_dict.update(d2)
    return new_dict


marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
}
student = {
    "sujal": 99,
    "anuj": 28,
    "zaid": 56,
    "sayali": 43,
}

ans = merge_dicts(marks, student)
print(ans)


"""
Q8.Create a dictionary of 6 subjects and their respective marks. Print the subject 
   with the highest marks and the one with the lowest, using max() and min() 
   functions alongside a lambda expression.
"""
students = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
    "sanskrit": 87,
}

Highest = max(students.items(), key=lambda x: x[1])
Lowest = min(students.items(), key=lambda x: x[1])
print(f"Highest Marks Subject : {Highest} and Lowest {Lowest}")


"""
Q9.Create a nested dictionary containing details for 4 students, where each 
   student entry includes their name, age, and city. Write a loop to print the full 
   details of each student in a clear, readable format
"""
students = {
    1: {"name": "Sujal", "age": 21, "city": "Pune"},
    2: {"name": "Rahul", "age": 22, "city": "Mumbai"},
    3: {"name": "Priya", "age": 20, "city": "Nashik"},
    4: {"name": "Amit", "age": 23, "city": "Nagpur"},
}

for entry, details in students.items():
    print(f"Student {entry}")
    print(f"Name : {details["name"]}")
    print(f"Age : {details["age"]}")
    print(f"City : {details["city"]}")
    print("-" * 20)


"""
Q10.Design a dictionary where each key is a student's name and the 
    corresponding value is a list of their marks in 3 different subjects. Calculate 
    and print the total marks and average marks for each student.
"""
students = {
    "sujal": [88, 96, 99],
    "sayali": [92, 73, 84],
    "anuj": [64, 88, 99],
    "manish": [77, 88, 66],
    "zaid": [88, 94, 83],
}


for student, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    #  print(f"The Total Marks {student} get is {total} and their Average is {average}")
    print(f"Student {student}")
    print(f"Total Marks : {total}")
    print(f"Average : {average:.2f}")
    print("-" * 20)


"""
Q11.Given a dictionary of subjects and their marks, sort it by marks in descending 
    order. Then, print only the top 3 subjects with the highest marks.
"""
students = {
    "science": 99,
    "maths": 56,
    "comp": 88,
    "hindi": 43,
    "history": 71,
    "sanskrit": 87,
}

ans = sorted(students.items(), key=lambda x: x[1], reverse=True)
result = ans[0:3]
for sub, mark in result:
    print(f"Subject : {sub} and Marks : {mark}")
    print("=" * 20)


"""
Q12.Using dictionary comprehension, create a new dictionary 
    where keys are numbers from 1 to 10 (inclusive), and values are the cube of each 
    number.
"""
cube = {i: i**3 for i in range(1, 11)}
print(cube)


"""
Q13.Given an existing dictionary of subjects and their respective marks, 
    use dictionary comprehension to generate a new dictionary that includes 
    only the subjects where the student scored 40 or more (i.e., passed).
"""
students = {
    "science": 99,
    "maths": 56,
    "comp": 20,
    "hindi": 43,
    "history": 23,
    "sanskrit": 87,
}

new_dict = {Sub: marks for Sub, marks in students.items() if marks >= 40}
print("Passed : ", new_dict)


"""
Q14.You have two separate lists: one containing subject names and another 
    containing corresponding marks. Create a dictionary from these two 
    lists using dictionary comprehension, mapping each subject to its mark
"""
subjects = ["math", "science", "english"]
scores = [85, 92, 78]

new_dict = {sub: m for sub, m in zip(subjects, scores)}
# print(new_dict)
for sub, m in new_dict.items():
    print(f"Subject : {sub} and Marks : {m}")
