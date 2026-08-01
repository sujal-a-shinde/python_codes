"""Q1. Print all the numbers which are divisible by 3 and 5, from 1 to 100."""

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

i = start
while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1

print(f"\nAfter the while loop, start value is {start}")

# Q2. Sum of all the numbers from 1 to 100.

num = int(input("Enter the your Start Number : "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i += 1

print(f"\nAfter the while loop, sum value is {sum}")

"""Q3. Sum of all the numbers from 1 to 100 divisible by 2 and 7."""

num = int(input("Enter the your Start Number : "))
sum = 0
i = 1
while i <= num:
    if i % 2 == 0 and i % 7 == 0:
        sum = sum + i
    i += 1


print("sum =", sum)

"""Q4. Ask a number from the user, print the multiplication table upto 10."""

num = int(input("Enter the your Start Number : "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

"""Q5. Ask a number from the user, and print all the factors"""

num = int(input("Enter the your Start Number : "))
i = 1
while i <= 10:
    if num % i == 0:
        print(i, end=" ")
    i += 1

"""Q6. Factorial of the number"""

num = int(input("Enter the your Start Number : "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact, end=" ")
