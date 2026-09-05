nums = [5, 7, 4, 64, 32, 17, 53, 85, 3, 1, 999]

for index, value in enumerate(nums):
    print(f"Index = {index} and Value = {value}")


for index, value in enumerate(nums):
    if value % 2 == 0:
        print(index)
