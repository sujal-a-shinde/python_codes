def greet(name, age):
    return f"Your name is {name} and age is {age} years"
    print("good")
    print("done")
    # above print will not return any output


print(greet("Sujal", 22))

# is prime or not
# Return True if a number is prime number return False


def is_prime(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


print(is_prime(21))
