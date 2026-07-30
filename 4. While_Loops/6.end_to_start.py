# 10 to 1


start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

i = end
while i >= start:
    print(i, end=" ")
    i -= 1

print(f"\nAfter the while loop, start value is {start}")
