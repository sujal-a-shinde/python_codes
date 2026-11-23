fruits = {"kiwi", "grape", "lichi", "apple", "mango"}

# Simple for loop

for fruit in fruits:
    print(fruit, end=" ")
print()
# Looping with enumerates

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
