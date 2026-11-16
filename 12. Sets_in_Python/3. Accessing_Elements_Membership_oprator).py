fruits = {"apple", "mango", "banana"}

print("apple" in fruits)  # True
print("cake" in fruits)  # False
print("kiwi" not in fruits)  # True


# Example

allowed_users = {"Sujal", "Anuj", "Sayali"}

users = input("Enter UserName : ")
if users in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")
