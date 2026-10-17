marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}


print(marks.items())

for detail in marks.items():
    sub = detail[0]
    mark = detail[1]
    print(sub, mark)


for sub, mark in marks.items():
    print(f"sub = {sub} and marks = {mark}")
