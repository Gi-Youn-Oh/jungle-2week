# 색종이의 배열은 1,4,8,16,32,64 정사각형 모양으로 차차 증가
# 4등분으로 규칙적으로 잘린다 > 반복 , 잘리는 조건 : 1등분이 모두 같은 수로 있지 않을때 잘린다.
# 각 등분의 첫인덱스를 기준으로 확인하면 된다.

import sys
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def solution(x,y,N):
    global white, blue
    color = board[x][y]
    for i in range (x,x+N):
        for j in range(y,y+N):
            if color != board[i][j]:
                solution(x,y,N//2)
                solution(x,y+N//2,N//2)
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        white+=1
    else:
        blue+=1

solution(0,0,N)
print(white)
print(blue)
