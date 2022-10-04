import sys
input= sys.stdin.readline

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

def mul(matrix1,matrix2):
    ans=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N): # 행
        for j in range(N): # 열
            for k in range(N): # 새롭게 곱해진 행렬의 원소
                ans[i][j] += matrix1[i][k]*matrix2[k][j] # 각 원소에 대한 새로운 값을 넣어준다.
            ans[i][j] %=1000
    return ans

def DoC(M,Matrix):
    if M==1:
        return Matrix
    elif M==2:
        return mul(Matrix,Matrix)
    else:
        tmp=DoC(M//2,Matrix)
        #홀수이면
        if M%2:
            return mul(mul(tmp,tmp),Matrix)
        else:
            return mul(tmp,tmp)

res = DoC(M,board)
for row in res:
    for cell in row:
        print(cell%1000,end=" ")
    print()