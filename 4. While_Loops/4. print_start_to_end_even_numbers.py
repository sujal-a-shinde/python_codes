# Print Start to End Even numbers

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

i = start
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print(f"\nAfter the while loop, start value is {start}")
