"""
Q1.Given a list of numbers, write Python code using a loop to find and
   print the largest element. Do not use the built-in max() function.
   # Example:
   # numbers = [3, 1, 4, 1, 5, 9, 2, 6]
   # Expected Output: The largest element is: 9
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]


maxi = float("-inf")
for num in numbers:
    if num > maxi:
        maxi = num
print(f"Largest number in List is : {maxi}")


# Minimum Number in list
maxi = float("inf")
for num in numbers:
    if num < maxi:
        maxi = num
print(f"Smallest number in List is : {maxi}")

"""
Q2.Write a program that takes a list and a target number.
   Use a loop to determine if the target number exists in the list.
   # Example:
   # my_list = [10, 20, 30, 40, 50]
   # target = 30
   # Expected Output: 30 exists in the list.
   # target = 60
   # Expected Output: 60 does not exist in the list.
"""

def does_target_exist(lst, target):
    for num in my_list:
        if num == target:
            return f"{target} Exist in the List"
    return f"{target} Does not Exist in the List"


my_list = [10, 20, 30, 40, 50]
print(does_target_exist(my_list, 30))
print(does_target_exist(my_list, 60))


"""
Q3.Given a list of numbers, use a loop to calculate
   and print their average. You can use len() to get the count of
   elements, but avoid using sum() for the total.
   Format the average to two decimal places.
   # Example:
   # scores = [85, 90, 78, 92, 88]
   # Expected Output: The average score is: 86.60
"""


def avg(lst):
    n = len(scores)
    total = 0
    for num in scores:
        total += num

    average = total / n
    return f"average"


scores = [85, 90, 78, 92, 88]

print(avg(scores))

"""
Q4.Given two lists of the same length, write Python code using a 
    loop to create a new list where each element is the sum of the 
    corresponding elements from both original lists.
   # Example:
   # list1 = [10, 20, 30, 40]
   # list2 = [1, 2, 3, 4]
   # Expected Output: [11, 22, 33, 44]
   # list_a = [5, 15, 25]
   # list_b = [2, 4, 6]
   # Expected Output: [7, 19, 31]
"""

def add_list(lst1, lst2):
    new_list = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list


list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
ans = add_list(list1, list2)
print(ans)


"""
Q5.Write a program that takes a list of numbers and, using a loop,
   determines whether it is sorted in ascending order.
   Print True if it is sorted, and False otherwise.
   Do not use built-in sort or sorted() functions for checking.
   # Example 1:
   # numbers = [1, 5, 10, 15, 20]
   # Expected Output: True
   # Example 2:
   # numbers = [1, 10, 5, 15, 20]
   # Expected Output: False
   # Example 3:
   # numbers = []
   # Expected Output: True (An empty list is considered sorted
"""


def is_sorted(lst):
    if lst == sorted(lst):
        return True
    return False


numbers = [1, 5, 10, 15, 20]
print(is_sorted(numbers))


def is_sorted(lst):
    n = len(lst)
    for i in range(0, n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


numbers = [1, 5, 10, 15, 20]
print(is_sorted(numbers))


"""
Q6.Find the largest and smallest number
   in a list without using built-in functions like
   max() or min().
   Hint: Use a loop and a variable to track the
   current largest/smallest as you go through
   the list. Example: if the list is [3, 1, 4, 1, 5],
   the largest is 5 and smallest is 1.
"""

def largest_and_smallest(lst):
    n = len(lst)
    maxi = float("-inf")
    for nums in lst:
        if nums > maxi:
            maxi = nums

    mini = float("inf")
    for nums in lst:
        if nums < mini:
            mini = nums

    return f"the largest is {maxi} and smallest is {mini}"


my_list = [3, 1, 4, 1, 5]
print(largest_and_smallest(my_list))


# """
# Q7.Reverse a list without using the
#   .reverse() method or list slicing ([::-1]).
#   Hint: Think about swapping elements from
#   both ends of the list using a loop.
#   Example: [1, 2, 3, 4, 5]
#   →
#    [5, 4, 3, 2, 1]
# """


def reverse_lisst(lst):
    n = len(lst)
    new_list = []
    for i in range(n - 1, -1, -1):
        new_list.append(lst[i])
    return new_list


my_list = [10, 2, 43, 54, 5]
print(reverse_lisst(my_list))


# """
# Q8. Given two lists, merge them into a
#     single new list without modifying the
#     originals.
#     Hint: Use the + operator or a loop to
#     combine. Example: list1 = [1, 2], list2 = [3,
#     4]
#     →
#      merged = [1, 2, 3, 4]

# """

def add_list(lst1, lst2):
    new_list = lst1 + lst2
    return new_list


list1 = [1, 2]
list2 = [3, 4]

print(add_list(list1, list2))

# method 2
def add_list(lst1, lst2):
    new_list = []
    for nums in lst1:
        new_list.append(nums)
    for nums in lst2:
        new_list.append(nums)

    return new_list


list1 = [1, 2]
list2 = [3, 4]

print(add_list(list1, list2))


# """
# Q9.Given a list, remove all duplicate elements while
#    preserving the original order of the unique items.
#    # Example input:
#    data = [10, 20, 30, 20, 10, 40, 50, 40]
#    # Expected output: [10, 20, 30, 40, 50]
# """


def remove_duplicate(lst):
    result = []
    for nums in lst:
        if nums not in result:
            result.append(nums)
    return result


data = [10, 20, 30, 20, 10, 40, 50, 40]
print(remove_duplicate(data))

# """
# Q10.Separate a list of integers into two distinct lists: one
#     containing all the even numbers and the other
#     containing all the odd numbers.
#     # Example input:
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # Expected output:
#     # evens = [2, 4, 6, 8, 10]
#     # odds = [1, 3, 5, 7, 9
# """


def even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(f"Even_List = {even}")
    print(f"Odd_List = {odd}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd(numbers)


# """
# Q11.Create a list containing the squares of numbers
#     from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
#     # Expected output:
#     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# """
def squ_num(lst):
    square_list = []
    for nums in lst:
        sqa = nums**2
        square_list.append(sqa)
    return square_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(squ_num(numbers))


# """
# Q12.Given a list of numbers (which may contain duplicates), write a
#     Python script that takes an integer as input from the user and
#     removes all occurrences of that integer from the list.
#     # Example input list:
#     my_list = [10, 20, 10, 30, 20, 10, 40]
#     # If user enters 10, expected output: [20, 30, 20, 40]
# """


def remove_dup(lst, target):
    new_list = []
    for nums in lst:
        if nums != target:
            new_list.append(nums)
    return new_list


n = int(input("Enter Your Number : "))
my_list = [10, 20, 10, 30, 20, 10, 40]
print(remove_dup(my_list, n))

# 2nd method
def remove_dup(lst, target):
    while target in lst:
        lst.remove(target)


n = int(input("Enter Your Number : "))
my_list = [10, 20, 10, 30, 20, 10, 40]
remove_dup(my_list, n)
print(my_list)


"""
Q13.Write a Python script that iterates through a list of integers and
    replaces every negative number found in the list with the value 0.
    # Example input list:
    numbers = [5, -3, 8, -1, 0, -10, 12]
    # Expected output: [5, 0, 8, 0, 0, 0, 12]
"""


def neg_replace(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


numbers = [5, -3, 8, -1, 7, -10, 12]
print(neg_replace(numbers))
