lst = ["Sujal", 54, 21.98, True, "Pune", 54, 54]

# append()
print(lst, id(lst))
lst.append(100)
lst.append("Delhi")
print(lst)

# insert()
lst.insert(2, "Shinde")
print(lst)

# pop()
lst.pop()  # by default remove last value
x = lst.pop()  # return the value
print(x)
lst.pop(0)
print(lst)  # remove by index

# remove()
lst.remove(54)  # remove by value
print(lst, id(lst))
