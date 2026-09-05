nums = [5, 7, 4, 64, 32, 17, 53, 85, 3, 1, 999]

n = len(nums)

sum = 0
for i in range(0, n):
    sum = sum + nums[i]
    # print(nums[i], end=" ")
print(sum)


for i in range(n - 1, 0, -1):
    print(nums[i], end=" ")


total = 0
for num in nums:
    total += num
print(total)


for num in nums[::-1]:
    print(num, end=" ")
