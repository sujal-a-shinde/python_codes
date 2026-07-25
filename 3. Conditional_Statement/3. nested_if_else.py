# Age >= 18
# Certificate = True

age = int(input("enter Your age : "))
Certificate = input("Certification:")

if age >= 18:
    if Certificate == "yes" or "Yes":
        print("You are Hired")
    else:
        print("you are not Hired because no certification")
else:
    print("you are not Hired because age is below 18")
