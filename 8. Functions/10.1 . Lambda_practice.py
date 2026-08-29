"""
Q1. Write a lambda function that takes a number and returns its cube. Store
          it in a variable and call it.
"""

cube = lambda num: num**3
print(cube(3))

"""
Q2. Write a lambda function that takes a number and returns "Positive", or 
          "Negative".
"""

is_check = lambda num: "Positive" if num >= 0 else "Negative"
print(is_check(2))
