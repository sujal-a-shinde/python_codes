# take 3 int as parameter , print the Total


def addition(a, b, c):
    print(f"Total = {a+b+c}")


addition(10, 24, 12)


# Ask name,age and gender , print them 


def greet(name, age, gender):
    print(f"hey! {name} and you are {age} and your gender is {gender}")


n = input("Enter Name : ")
a = int(input("Enter Age : "))
g = input("Enter Gender : ")

greet(n, a, g)
