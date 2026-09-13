# Make a new list from 1 to 10 -> [1,2,3,4,5,6,7,8,9,10]

# new_list = [i for i in range(1, 11)]
new_list = [i for i in range(10, 0, -1)]
print(new_list)


# 1 to 10 but all squared -> [1,4,9,16,25,36,49,64,81,100]

new_list = [i**2 for i in range(1, 11)]
print(new_list)


# 1 to 20 , but only even numbers

new_list = [i for i in range(1, 21) if i % 2 == 0]
print(new_list)


# 1 to 20 , but 2 and 5 divisible numbers

new_list = [i for i in range(1, 21) if i % 2 == 0 and i % 5 == 0]
print(new_list)


# 2 to 100 , but prime numbers only
def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


new_list = [i for i in range(1, 101) if is_prime(i) == True]
print(new_list)
