"""
Q1. Write a function called add that takes two numbers as parameters
         and prints their sum
"""


def add(a, b):
    print(f"Total = {a+b}")


num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
add(num1, num2)

"""
Q2. Write a function called rectangle_area that takes length and breadth 
         as parameters and prints the area.
"""


def rectangle_area(length, breadth):
    area = length * breadth
    print(f"Area = {area}")


L = int(input("Enter 1st Number : "))
B = int(input("Enter 2nd Number : "))
rectangle_area(L, B)


"""
Q3.  Write a function called find_max that takes three numbers as 
          parameters and prints the largest one.
"""


def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"{n1} is Largest Number")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is Largest Number")
    else:
        print(f"{n3} is Largest Number")


num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3nd Number : "))
find_max(num1, num2, num3)


"""
Q4. Write a function called discount_price that takes original_price 
          and discount_percent as parameters and prints the final 
          price after discount.
"""


def discount_price(original_price, discount_percent):
    discount_price = original_price * (discount_percent / 100)
    final_price = original_price - discount_price
    print(f"Final Amount = {final_price}")


original_amt = int(input("Enter Number : "))
discount_pst = int(input("Enter Number : "))
discount_price(original_amt, discount_pst)


