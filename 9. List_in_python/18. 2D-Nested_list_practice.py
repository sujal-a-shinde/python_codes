"""
Q1.Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements.
   # Example:
   # matrix = [
   #     [1, 2, 3],
   #     [4, 5, 6],
   #     [7, 8, 9]
   # ]
   # Expected output for this example: 45
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# total = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         total += matrix[i][j]
#     #     print(matrix[i][j],end=" ")
#     # print()
# print(total)


"""
Q2.Given a 3x3 matrix as input, print its lower triangle. Replace all elements in 
the upper triangle (above the main diagonal) with an asterisk (*).
   # Input:
   # 1 2 3
   # 4 5 6
   # 7 8 9
   # Expected Output:
   # 1 * *
   # 4 5 *
   # 7 8 9
"""
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[0][1]:
#             for nums in matrix:
#                 matrix[0][1] = "*"

#         if matrix[0][2]:
#             for nums in matrix:
#                 matrix[0][2] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[1][2] = "*"

#         print(matrix[i][j], end=" ")
#     print()

# Another method efficient

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0, r):
#     for j in range(0, c):
#         if i >= j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q3.Given a 3x3 matrix, print its upper triangle. Replace all elements in 
   the lower triangle (below the main diagonal) with an asterisk (*).
   # Input:
   # 1 2 3
   # 4 5 6
   # 7 8 9
   # Expected Output:
   # 1 2 3
   # * 5 6
   # * * 9
"""
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[1][0]:
#             for nums in matrix:
#                 matrix[1][0] = "*"

#         if matrix[2][0]:
#             for nums in matrix:
#                 matrix[2][0] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[2][1] = "*"

#         print(matrix[i][j], end=" ")
#     print()

# Another method

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0, r):
#     for j in range(0, c):
#         if i <= j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q4.Given a 3x3 matrix, print only the main diagonal elements and 
   replace everything else with an asterisk (*).
   # Input:
   # 1 2 3
   # 4 5 6
   # 7 8 9
   # Expected Output:
   # 1 * *
   # * 5 *
   # * * 9
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[1][0]:
#             for nums in matrix:
#                 matrix[1][0] = "*"

#         if matrix[2][0]:
#             for nums in matrix:
#                 matrix[2][0] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[2][1] = "*"

#         if matrix[0][1]:
#             for nums in matrix:
#                 matrix[0][1] = "*"

#         if matrix[0][2]:
#             for nums in matrix:
#                 matrix[0][2] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[1][2] = "*"

#         print(matrix[i][j], end=" ")
#     print()

# another method

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0, r):
#     for j in range(0, c):
#         if i == j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()


"""
Q5.Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left) 
   elements and replace everything else with an asterisk (*).
   # Input:
   # 1 2 3
   # 4 5 6
   # 7 8 9
   # Expected Output:
   # * * 3
   # * 5 *
   # 7 * *
"""
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(0, 3):
#     for j in range(0, 3):
#         if matrix[0][0]:
#             for nums in matrix:
#                 matrix[0][0] = "*"

#         if matrix[0][1]:
#             for nums in matrix:
#                 matrix[0][1] = "*"

#         if matrix[1][0]:
#             for nums in matrix:
#                 matrix[1][0] = "*"

#         if matrix[2][2]:
#             for nums in matrix:
#                 matrix[2][2] = "*"

#         if matrix[2][1]:
#             for nums in matrix:
#                 matrix[2][1] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[1][2] = "*"

#         print(matrix[i][j], end=" ")
#     print()

#  another method

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0, r):
#     for j in range(0, c):
#         if i + j == r - 1:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q6.Given a 4x4 matrix, print only the border elements and replace the inner 
   elements with an asterisk (*).
   # Input:
   # 1  2  3  4
   # 5  6  7  8
   # 9  10 11 12
   # 13 14 15 16
   # Expected Output:
   # 1  2  3  4
   # 5  *  *  8
   # 9  *  *  12
   # 13 14 15 1
"""
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]


# rows = len(matrix)
# columns = len(matrix[0])
# for i in range(0, rows):
#     for j in range(0, columns):
#         if matrix[1][1]:
#             for nums in matrix:
#                 matrix[1][1] = "*"

#         if matrix[1][2]:
#             for nums in matrix:
#                 matrix[1][2] = "*"

#         if matrix[2][1]:
#             for nums in matrix:
#                 matrix[2][1] = "*"

#         if matrix[2][2]:
#             for nums in matrix:
#                 matrix[2][2] = "*"

#         print(matrix[i][j], end=" ")
#     print()


# r = len(matrix)
# c = len(matrix[0])

# # for i in range(0, r):
# #     for j in range(0, c):
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(matrix[i][j] = "*")
#     print()
