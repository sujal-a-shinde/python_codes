# 1 to 10
# i=5 loop stop

i = 1
while i <= 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1


for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

for i in range(1, 11):
    print(i, end=" ")
    if i == 5:
        break
