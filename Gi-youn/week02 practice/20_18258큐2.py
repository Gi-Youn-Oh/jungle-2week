from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

q = deque([])

for _ in range(N):
    word = input().split() # 입력받는데 split해서 입력 받기
    if word[0] == 'push':
            q.append(word[1])
    elif word[0] == 'pop':
        if len(q):
            print(q.popleft())
        else :
            print(-1)
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        if len(q):
            print(0)
        else :
            print(1)
    elif word[0] == 'front':
        if len(q):
            print(q[0])
        else :
            print(-1)
    elif word[0] == 'back':
        if len(q): 
            print(q[-1])
        else:
            print(-1)


