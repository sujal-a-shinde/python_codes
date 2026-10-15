marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}

print(marks.values())

for mark in marks.values():
    print(f" marks = {mark}")

total = 0
for mark in marks.values():
    total += mark
print(f" Total = {total}")
