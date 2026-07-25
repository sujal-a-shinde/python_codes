"""
Q1: Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator.
"""

num = int(input("Enter your Number : "))
print(num % 2 == 0)

"""
Q2: Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

age = int(input("Enter your age = "))
can_vote = age >= 18
senior_citizen = age >= 60

print(f"User can vote = {can_vote}")
print(f"User is senior citizen = {senior_citizen}")

"""
Q3: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""
Sub1 = int(input("Enter your English Marks : "))
Sub2 = int(input("Enter your Science Marks : "))
Sub3 = int(input("Enter your Maths Marks : "))

Total = Sub1 + Sub2 + Sub3
Average = Total / 3

print(f"The Total Marks in 3 Subjects is {Total} \nThe Average is {Average:.2f}")

"""Q4: Take a number as input. Print the result of that number raised to the 
power of 3 using **. Also print what // 7 and % 7 give for the same number."""

num = int(input("Enter your Number : "))
print(
    f"The power of number is {num**3}\nand its Floor Division is {num//7}\nand it gives the Remainder of {num%7}"
)

"""Q5: Take two numbers as input. Without using *, calculate and print their product 
using += in a way that adds the first number to itself the 
second number of times. (Think carefully.)"""

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

product = 0

for i in range(num2):
    product += num1

print("Product =", product)
