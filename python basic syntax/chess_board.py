"""
Given two numbers n and m. Create a two-dimensional array of size (n×m) and populate it with the characters "." and "*"
in a checkerboard pattern. The top left corner should have the character "." .
"""


n, m = [int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (j+1) % 2 == 0 and (i + 1) % 2 != 0:
            a[i][j] = '*'
        if (i + 1) % 2 == 0 and (j+1) % 2 != 0:
            a[i][j] = '*'

for row in a:
    print(' '.join([str(elem) for elem in row]))
