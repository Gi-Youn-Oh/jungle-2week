# 전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수)

# 입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에는 전체 종이의 한 변의 길이 N
# N은 2, 4, 8, 16, 32, 64, 128 중 하나
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력

import sys

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

# x,y 에서 시작하고 길이가 N이다.


def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solution(0, 0, N)
print(result.count(0))
print(result.count(1))
