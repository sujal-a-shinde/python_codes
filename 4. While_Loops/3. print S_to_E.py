# Start to End by user
# start to end print using while loop

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))

i = start
while i <= end:
    print(i, end=" ")
    i += 1

print(f"\nAfter the while loop, start value is {start}")
