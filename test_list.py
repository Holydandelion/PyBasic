
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


print(matrix[0])

#4 * 3 矩阵， 先取行在取列
print([[row[i] for row in matrix] for i in range(4)])
print(matrix[1][3])

L = [1, 2, 3, 4, 5, 6]
print(L[:3])
print(L[4:])

print(L.extend([7,8,9]))
print(L.reverse())

del L[len(L) - 1]
del L[:len(L)//2]
print(L)
del L