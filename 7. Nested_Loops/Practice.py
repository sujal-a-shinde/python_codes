"""
Q1
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

num = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


"""
Q2
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()


"""
Q3
* * * * *
*       *
*       *
*       *
* * * * *
"""
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 5 or j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Q4
* 
* *  
*   *  
*     *
* * * * * 
"""
for i in range(1, 6):
    for j in range(1, 6):
        if i == 5 or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Q5
* * * * * * 
*         *
*         *
* * * * * *
"""

for i in range(1, 5):
    for j in range(1, 7):
        if i == 4 or i == 1 or j == 1 or j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Q6
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""

for i in range(1, 6):
    for j in range(1, 6):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()


"""
Q7
        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 
"""
for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        if j == 1 or j == i * 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(4, 0, -1):
    for k in range(1, 5 - i + 1):
        print(" ", end=" ")
    for j in range(1, i * 2):
        if j == 1 or j == i * 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

