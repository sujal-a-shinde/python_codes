"""
Q1. Write a function that ask a number from user and prints if that
          number is odd or even.
"""


def even_odd():
    is_check = "Even" if num % 2 == 0 else "Odd"
    print(is_check)

num = int(input("Enter Your Number : "))
even_odd()

"""
Q2. Write a function that print all the factors of a number entered by user.
"""


def factors():
    num = int(input("Enter Your Number : "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


factors()

"""
Q3. Write a function fizzbuzz(n) that takes a single number and prints "Fizz" 
          if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible 
          by both, otherwise print the number itself.
"""


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n


num1 = int(input("Enter your Single Number : "))
print(fizzbuzz(num1))


"""
Q5. Write a function power(base, exp) that returns base raised to exp using a 
loop - no ** operator or pow() allowed
"""


def power(base, exp):
    if exp < 0:
        base = 1 / base
        exp = -exp

    pw = 1
    for i in range(exp):
        pw *= base
    return pw


num1 = int(input("Enter your Base Number : "))
num2 = int(input("Enter your Exponent Number : "))

print(power(num1, num2))


"""
Q6. Write a function tax_calculator(income) that takes annual income and returns 
          the tax amount based on these slabs:
Up to 2,50,000 → No tax
2,50,001 to 5,00,000 → 5%
5,00,001 to 10,00,000 → 20%
Above 10,00,000 → 30%
"""


def tax_calculator(income):
    if income <= 2_50_000:
        tax = "No Tax"
    elif income > 2_50_000 and income <= 5_00_000:
        tax = income * 0.05
    elif income > 5_00_000 and income <= 10_00_000:
        tax = income * 0.20
    elif income > 10_00_000:
        tax = income * 0.30

    in_hand_Annual_income = income - tax
    # print(f"The in hand income is {in_hand_Annual_income} and tax applied {tax}")

    return f"The in hand income is {in_hand_Annual_income} and tax applied {tax}"


# in_hand_Annual_income = income - tax

n = int(input("Enter Your Annual_income : "))
print(tax_calculator(n))
