# Make a function which returns min and max of a tuple


def min_max(tup):
    # maxi=float("-inf")
    maxi = max(tup)
    mini = min(tup)
    # for maxi in tup:
    #     maxi = max(tup)

    # for mini in tup:
    #     mini = min(tup)
    # return maxi, mini
    return maxi, mini


my_tuple = 1, 2, 3, 4
# print(min_max(my_tuple))
ans1, ans2 = min_max(my_tuple)
print(f"Maximum : {ans1} and Minimum : {ans2}")
 