"""
Given an integer n, produce a two-dimensional array of size (n×n) and complete it according to the following rules,
and print with a single space between characters:
On the main diagonal write 0 .
On the diagonals adjacent to the main, write 1 .
On the next adjacent diagonals write 2 and so forth.
Print the elements of the resulting array.
"""


n = int(input())
a = [[abs(i-j) for j in range(n)] for i in range(n)]

print('\n'.join(' '.join(str(i) for i in r) for r in a))