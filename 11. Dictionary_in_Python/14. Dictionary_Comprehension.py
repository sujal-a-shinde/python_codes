# Square from 1 to 10 using dict comprehension {1 : 1,2: 4}

square = {i: i * i for i in range(1, 11)}
print(square)

# With condition
marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

# Keep only subject with marks > 80
top = {sub: m for sub, m in marks.items() if m > 80}
print(top)

# Transform -- double of Marks
double = {sub: m * 2 for sub, m in marks.items()}
print(double)


# zip() "Creating a dict from two lists"
subjects = ["math", "science", "english"]
scores = [85, 92, 78]

result = {sub: scr for sub, scr in zip(subjects, scores)}
print(result)
