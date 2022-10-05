import sys


input = sys.stdin.readline

N = int(input())

paper = []

for _ in range(N):
    block = list(map(int, input().split()))
    paper.append(block)

colorPaper_list = []

# 2차원리스트를 좌표로 생각해라 ( 사분면이라고 생각 )


def find(x, y, N):
    first = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if first != paper[i][j]:
                find(x, y, N//2)
                find(x+N//2, y, N//2)
                find(x, y+N//2, N//2)
                find(x+N//2, y+N//2, N//2)
                return
    if first == 0:
        colorPaper_list.append(0)
    else:
        colorPaper_list.append(1)


find(0, 0, N)
print(colorPaper_list.count(0))
print(colorPaper_list.count(1))
