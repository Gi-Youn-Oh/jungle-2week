import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

deq = deque()  # 재할당 개념 공부

for _ in range(T):
    command = input().split()

    if command[0] == "push":
        deq.append(int(command[1]))

    if command[0] == "pop":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    if command[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(int(deq[0]))

    if command[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(int(deq[-1]))

    if command[0] == "empty":
        if len(deq) != 0:
            print(0)
        else:
            print(1)
    if command[0] == 'size':
        print(len(deq))
