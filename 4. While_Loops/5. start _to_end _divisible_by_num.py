# Print Start to End,numbers that are divisible by 3 and 4

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
    i += 1

print(f"\nAfter the while loop, start value is {start}")
