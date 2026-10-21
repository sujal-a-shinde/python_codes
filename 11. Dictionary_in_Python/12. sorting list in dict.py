marks = {
    "akshy": [43, 12, 98, 10, 22],
    "priya": [76, 55, 34, 89, 61],
    "rahul": [20, 45, 67, 30, 88],
    "sneha": [91, 73, 50, 14, 62],
    "karan": [38, 82, 47, 95, 29],
}

ans = dict(
    sorted(marks.items(), key=lambda x: x[1][4])
)  # it will work only with uniform list[4]
print(ans)


marks = {
    "akshy": [43, 12, 98, 10, 22],
    "priya": [76, 55, 34, 89, 61],
    "rahul": [20, 45, 67, 30],
    "sneha": [91, 73],
    "karan": [38, 82, 47, 95, 29],
}

ans = dict(
    sorted(marks.items(), key=lambda x: x[1][-1])
)  # it will work when uniform list is not there[-1]
print(ans)


ans = dict(sorted(marks.items(), key=lambda x: sum(x[1])))
print(ans)  # sorted by sum of list # Accesending
 
ans = dict(sorted(marks.items(), key=lambda x: sum(x[1]), reverse=True))
print(ans) #decending
