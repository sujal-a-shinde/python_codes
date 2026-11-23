# Pyhton Offers Methods Like
# remove(), discard(), pop() and clear()

pythonfruits = {"kiwi", "grape", "lichi", "apple", "mango"}
pythonfruits.remove(
    "apple"
)  # Remove specific elements but give Error when elements does not exist
pythonfruits.discard(
    "apple"
)  # Remove specific elements but does not give Error when elements does not exist


pythonfruits.pop()  # Remove Specific Elements from the set

pythonfruits.clear()  # Clear all the Elements in set And give Empty set
print(pythonfruits)
