"""
90 above > A
81 - 90 > B
71 - 80 > C
61 - 70 > D
60 and below > Fail
"""

English = int(input("Enter Your English_marks :"))
Maths = int(input("Enter Your Math_marks :"))
Science = int(input("Enter Your Science_marks :"))

Total = English + Maths + Science

if Total >= 91 and Total<= 100:
    print("Grade A")
elif Total >= 81 and Total <= 90:
    print("Grade B")
elif Total >= 71 and Total <= 80:
    print("Grade C")
elif Total >= 61 and Total <= 70:
    print("Grade D")
elif Total >= 0 and Total <= 60:
    print("Fail")

else: 
    print("Invaild Marks Input")
