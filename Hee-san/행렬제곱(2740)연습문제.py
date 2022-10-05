import sys

input = sys.stdin.readline


# 2차원 배열 받는법에 익숙해지자. 이렇게 간단하게 쓸 수 있다.
a, b = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(a)]

b, d = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(b)]

# first_matrix = []
# second_matrix = []

# a, b = map(int, input().split())
# for _ in range(a):
#     mat = list(map(int, input().split()))
#     first_matrix.append(mat)


# c, d = map(int, input().split())
# for _ in range(c):
#     mat = list(map(int, input().split()))
#     second_matrix.append(mat)

# print(first_matrix)
# print(second_matrix)


AxB = [[0]*d for _ in range(a)]
print(matrixA)
print(matrixB)
print(AxB)
for row in range(a):
    for col in range(d):
        e = 0
        for i in range(b):
            e = e + matrixA[row][i] * matrixB[i][col]
            AxB[row][col] = e

for r in AxB:
    print(*r)



