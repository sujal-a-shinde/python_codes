marks = [23, 12, 5, 3, 33, 11]

# to get length of list
n = len(marks)
print(f"Length of list : {n}")


# Max and Min  '''it not work here when there is an string present in the list'''
m = max(marks)
print(f"Maximum Number in list : {m}")

mini = min(marks)
print(f"Minimum Number in list : {mini}")

total = sum(marks)
print(f"Total of Number in list : {total}")

# to sort using sorted(), it will always return you a new list

'''acesending'''
new_list = sorted(marks)
print(f"Sorted list : {new_list}")

'''Desending'''
new_list = sorted(marks, reverse=True)
print(f"Sorted list : {new_list}")
