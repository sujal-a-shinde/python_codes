# Local Variable
def addition(n1, n2, n3):
    total = n1 + n2 + n3
    print(f"The total is {total}")


addition(10, 20, 30)


# Local Variable 2
def xyz(n1, n2):
    n1 = 100  # Local Variables 'which only run in function '
    n2 = 200  # Local Variables
    print(f"Inside function n1={n1} and n2={n2}")


n1 = 10  # Globle Variables "have no relation with Local varibles"
n2 = 20
xyz(n1, n2)
print(n1)
print(n2)
