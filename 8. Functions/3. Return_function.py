def addition(n1, n2, n3):
    return n1 + n2 + n3


ans = addition(10, 24, 12)
print(ans)

# True or False return, if user can vote or not


def can_vote(age):
    if age >= 18:
        return True
    else:
        return False


ans1 = can_vote(23)
print(ans1)
