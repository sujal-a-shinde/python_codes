"""Q1. Print all the numbers which are divisible by 3 and 5, from 1 to 100."""

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

sum = 0
for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        sum += i
print(sum, end=" ")


"""Q2. Ask a number from the user, print the multiplication table upto 10."""

num = int(input("Enter the your Number : "))
end = int(input("Enter the your End Number : "))
for i in range(1, end + 1):
    print(f"{num} x {i} = {num * i}")


"""Q3. Factorial of the number"""

num = int(input("Enter the your Start Number : "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact, end=" ")
