# Start and End, print start to end

start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))
steps = int(input("Enter the your End Number : "))

for i in range(start, end + 1, steps):
    print(i, end=" ")

# Total
start = int(input("Enter the your Start Number : "))
end = int(input("Enter the your End Number : "))
steps = int(input("Enter the your step Number : "))

total = 0
for i in range(start, end + 1, steps):
    total += i
print(total)
