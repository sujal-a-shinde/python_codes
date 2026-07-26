"""Q1: Take a number as input. Print whether it is positive, negative, or zero"""

num = int(input("Enter your Number : "))

if num > 0:
    print("Positive")
elif num < 0:
    print("negative")
else:
    print("Zero")

'''Q2: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."'''

num1 = int(input("Enter your Number 1 : "))
num2 = int(input("Enter your Number 2 : "))

if num1 > num2:
    print(f"{num1} is Greater")
elif num2 > num1:
    print(f"{num2} is Greater")
else:
    print(f"{num1==num2}, both numbers are equal")

"""Q3: Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400."""

year = int(input("Enter year : "))

if (year % 4 == 0 and year % 100 != 0) and (year % 400 == 0):
    print("leap year")
else:
    print("Not a leap year")

"""Q4: Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message."""

age = int(input("Enter your Age : "))
valid_Id = input("Do you have Valid_ID : ")

if age >= 18:
    if valid_Id == "yes" or "Yes":
        print('"WELCOME"You can enter a Venue')
    else:
        print("You cant enter in the venue")
else:
    if age < 18 and valid_Id == "no" or "No":
        print("You are Minor and you Dont have Valid_Id")

"""Q5: Take three numbers as input. Print the largest of the three without using any
built-in function"""

num1 = int(input("Enter your number 1 :"))
num2 = int(input("Enter your number 2 :"))
num3 = int(input("Enter your number 3 :"))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is:{largest}")

"""Q6: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line."""

num = int(input("Enter your Number : "))
is_check = "Even" if num % 2 == 0 else "odd"
print(is_check)

"""Q7: A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount"""

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
elif amount > 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)
