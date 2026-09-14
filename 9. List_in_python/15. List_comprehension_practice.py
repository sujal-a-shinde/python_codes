"""
Q1.Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
   # Expected output:
   # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
"""

odd_sqr = [i * i for i in range(1, 21) if i % 2 != 0]
print(odd_sqr)

"""
Q2.Given a list of marks, use list comprehension to create a new list 
   that contains only the marks that are above 75.
   # Example input:
   marks = [65, 80, 70, 90, 75, 82, 60]
   # Expected output:
   # [80, 90, 82]
"""
marks = [65, 80, 70, 90, 75, 82, 60]
new_marks = [nums for nums in marks if nums >= 75]
print(new_marks)
