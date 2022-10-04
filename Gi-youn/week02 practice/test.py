
N = 5

def mul(matrix1,matrix2):
    ans=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N): # 행
        for j in range(N): # 열
            for k in range(N): # 새롭게 곱해진 행렬의 원소 
                ans[i][j] += matrix1[i][k]*matrix2[k][j] #각원소에 대한 표현
            ans[i][j] %=1000
    return ans

#     # 행렬의 곱 이해하기
# tmp=DoC(M//2,Matrix) 
# 이해하기