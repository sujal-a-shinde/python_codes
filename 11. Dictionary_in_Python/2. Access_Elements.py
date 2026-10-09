marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}
print(marks["science"])

# Alternate way to Access the dictionary (through methods)
print(marks.get("science"))

# none =0 if there is no key present in dictionary

print(marks.get("sciencee", 0))


# Question

subject = input("Enter your subject : ")

ans = marks.get(subject)
if ans is None:
    print("Subject not Found")
else:
    print(f"Marks Scored : {ans}")
