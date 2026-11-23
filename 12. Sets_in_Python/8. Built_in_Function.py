num = {40, 10, 30, 20, 50}

print(len(num))  # Output: 5 (number of elements)
print(min(num))  # Output: 10 (smallest elements)
print(max(num))  # Output: 50 (Largest elements)
print(sum(num))  # Output: 150 (sum of elements)

# sorted()

print(sorted(num))  # Accesding
print(sorted(num, reverse=True))  # Descending

# Type conversion

my_list = [1, 2, 3, 2, 1]
my_set = set(my_list)  # Converts list to set: {1, 2, 3}
print(my_set)
back_list = list(my_set)  # Converts set back to list: [1, 2, 3]
print(back_list)
my_tuple = tuple(my_set)  # Converts set to tuple: (1, 2, 3)
print(my_tuple)
