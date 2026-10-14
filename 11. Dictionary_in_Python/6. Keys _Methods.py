marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}

print(marks.keys())


total = 0
for sub in marks:

    # print(sub, marks[sub])
    print(f"Subject : {sub} and Marks : {marks[sub]}")
    total += marks[sub]

print(f"Total = {total}")
