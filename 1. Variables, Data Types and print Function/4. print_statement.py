Name = "Sujal"
age = 20
gender = "Male"

# print("Hello",Name,"and i am",age,"years old and my gender is",gender)
# print("Hello "+ Name +" and i am "+ age +" years old and my gender is "+ gender)


# 'sep' is used in betwwen the variables
print(Name, age, gender, sep="-")


# 'end' is used to end with specific
print(Name, end=" ")
print(age)
print(gender)

# F-strings
"""print(f"Your name is {Name}, and your age is {age}, your gender is {gender}")"""

print(f"Your name is {Name}, and your age is {age+24}, your gender is {gender}")
