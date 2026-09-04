lst = [56, 32, 12, 43, 77, 67, 34, 13, 24, 36, 68]
n = len(lst)

a = lst[0:4]
b = lst[5:8]
c = lst[1:10]
d = lst[1:88]
e = lst[5:6]
f = lst[5:5]  # empty list
g = lst[4:]
h = lst[:3]
i = lst[0:9:2]
j = lst[::4]

print(a, b, c, d, e, f, g, h, i, j, sep="\n")


lst = [56, 32, 12, 43, 77, 67, 34, 13, 24, 36, 68]
n = len(lst)

a = lst[9:3:-1]
b = lst[5:1:-1]
c = lst[::-1]
d = lst[::-2]

print(a, b, c, d, sep="\n")
