marks = {"math": 85, "science": 92, "english": 90, "hindi": 78}

ans = sorted(marks.items(), key=lambda x: x[0])  # sorted by Alphabets
print(ans)
ans = sorted(marks.items(), key=lambda x: x[1])  # sorted by values
print(ans)


ans = dict(sorted(marks.items(), key=lambda x: x[1]))  # Converted in Dictionary
print(ans)
