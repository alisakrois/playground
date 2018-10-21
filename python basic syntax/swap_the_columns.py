"""
Given two positive integers m and n, m lines of n elements, giving an m×n matrix A,
followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.
Write a function swap_columns(a, i, j) and call it to exchange the columns.
"""

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]


def swap_columns(a, i, j):
    for x in range(n):
        a[x][i], a[x][j] = a[x][j], a[x][i]
    for row in a:
        print(' '.join([str(elem) for elem in row]))


swap_columns(a, i, j)