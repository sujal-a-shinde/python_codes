"""
Q1.Create a list of 5 of your favourite movies. Print the first, last, and middle movie
from your list using both positive and negative indexing where appropriate.
# Example Output (using hypothetical movie list):
# First movie: The Shawshank Redemption
# Last movie: Forrest Gump
# Middle movie: The Matrix
"""

lst_movies = ["Interstellar", "Moonfall", "Terminator", "Geostorm", "The Matrix"]

n = len(lst_movies)
print(f"The First Movie  :{lst_movies[0]}")
print(f"The Last Movie  :{lst_movies[n-1]}")
print(f"The Middle Movie  :{lst_movies[n//2]}")


"""
Q2.Create a list of 5 numbers (e.g., [10, 20, 30, 40, 50]). Replace the second 
and fourth elements of this list with the number 0 using indexing. 
Print the updated list.
# Expected Output (for the example list above):
# [10, 0, 30, 0, 50]
"""

num = [10, 20, 30, 40, 50]

num[1] = 0
num[3] = 0
print(num)
