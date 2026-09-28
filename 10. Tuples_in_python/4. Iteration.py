my_tuple = (46, 52, 63, "Sujal", "Shinde", "Pune", 99)

n = len(my_tuple)
for i in range(0, n):
    print(my_tuple[i], end=" ")

print()
for ele in my_tuple:
    print(ele, end=" ")

print()
for index, value in enumerate(my_tuple):
    print(f"Index = {index} and Value = {value}")


''' Almost Everthing is same as list just we cannot update the tuple just we can used 
    min(),max(),index(),count(),sorted(),reverse(),slicing() etc
'''
