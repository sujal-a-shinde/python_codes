"""
Q1. Create a tuple of 5 of your favourite songs.
Print the first, last, and middle one using indexing.
"""

my_tuple = "tere bina", "finding her", "Paro", "Sahiba", "Ektrfa"

n = len(my_tuple)
print(
    f"First song : {my_tuple[0]} \nLast song: {my_tuple[-1]}\nMiddle Song : {my_tuple[n // 2]}"
)

"""
Q2. Create a tuple of 8 numbers. Using slicing, 
print the first 3, last 3, and every alternate element.
"""
my_tuple = 23, 13, 34, 54, 56, 67, 78, 100
n = len(my_tuple)
print(
    f"First 3 Elements : {my_tuple[0:3]}\nLast 3 Elements : {my_tuple[-1:-4:-1]}\nAlternate Elements : {my_tuple[0:n:2]}"
)


"""
Q3. Create a tuple of marks of 6 subject. Print the highest, lowest, total, and average.
"""


def student_marks(tup):
    n = len(tup)

    maxi = max(tup)
    mini = min(tup)

    # total =sum(tup)
    total = 0
    for nums in tup:
        total += nums

    average = total / n

    return f"The Highest Marks Student get is {maxi}\nthe Lowest Marks Student get is {mini}\nThe Total is {total}\nAverage is {average}"


marks = 78, 87, 65, 89, 88
print(student_marks(marks))


"""
Q4.: Take 5 numbers as input from the user, store them in a tuple,
and print the tuple along with its minimum and maximum
"""

a, b, c, d, e = map(int, input("Enter three numbers: ").split())

my_tuple = a, b, c, d, e

maxi = max(my_tuple)
mini = min(my_tuple)
print(f"My Tuple {my_tuple}\nThe Maximum Number is {maxi} and Minimum Number is {mini}")


"""
Q5.Write a function get_stats(nums) that takes a tuple of 
numbers and returns a tuple containing the sum, average, minimum, and maximum. Unpack 
the returned tuple and print each value
"""


def get_stats(nums):
    n = len(nums)
    Total = sum(nums)
    Average = Total / n
    Maxi = max(nums)
    Mini = min(nums)
    return Total, Average, Maxi, Mini


my_tuple = 23, 12, 25, 67, 78, 89
total, Avg, Max, Min = get_stats(my_tuple)

print(f"Total = {total}", type(total))
print(f"Average = {Avg}")
print(f"Maximum = {Max}")
print(f"Minimum = {Min}")
