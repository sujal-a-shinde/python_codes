"""
Q1. Write a function called square that takes a number and returns its square.
         Store the result and print it.
"""


def square(num):
    return num**2


n = int(input("Enter your number : "))
print(square(n))


"""
Q2. Write a function called min_of_three that takes three numbers and returns 
          the smallest without using any built-in function.
"""


def min_of_three(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return f"{n1} is Smallest"
    elif n2 < n1 and n2 < n3:
        return f"{n2} is Smallest"
    return f"{n3} is Smallest"


a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3nd number : "))
print(min_of_three(a, b, c))


"""
Q3. Write a function called absolute_value that takes a number and returns 
          its absolute value without using the built-in abs() function.
"""


def absolute_value(num):
    # return abs(num)
    if num >= 0:
        return num
    return num * -1


n = int(input("Enter your number : "))
print(absolute_value(n))
