my_tuple = (1, 2, 3, 4)  # packed [same for list]
my_tuple = 1, 2, 3, 4
my_tuple = (1,)  # give coma to make the single int into tuple
print(my_tuple, type(my_tuple))

# unpacking [same for list]
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d, type(a))

a, b, c, d = [1, 2, 3, 4] #list
print(a, b, c, d, type(a))
