"""Q1. Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)"""

total = 0
while True:
    a = int(input("Enter your number: "))
    if a < 0:
        continue
    elif a == 0:
        break
    total += a
print(total)


"""1st method"""
total = 0
for i in range(10**9):
    num = int(input("Enter Your Number : "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)

"""2nd method"""

total = 0
n = int(input("How many number do u want enter : "))
for i in range(n):
    num = int(input("Enter Your Number : "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)
