# 행렬의 곱셈 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def multi(matrix_1, matrix_2): # 행렬의 곱셈 정의
    ans = [[0 for _ in range(N)] for _ in range(N)] # 빈행렬 0으로 가득찬 행렬 임의로 만들기
    for i in range(N) : #행
        for j in range(N): #열
            for k in range(N): # 행과 열의 곱으로 만들어진 새로운 행렬
                ans[i][j] += matrix_1[i][k]*matrix_2[k][j] # 0 + 행열의 곱 원소 
            ans[i][j] %= 1000
    return ans
def doc(M,matrix):
    if M == 1:
        return matrix
    elif M == 2:
        return multi(matrix,matrix)
    else:
        tmp = doc(M//2,matrix)
        if M % 2== 0:
            return multi(tmp,tmp)
        else : 
            return multi(multi(tmp,tmp),matrix)

res = doc(M,arr)
for row in res:
    for cell in row:
        print(cell%1000,end =' ')
    print()