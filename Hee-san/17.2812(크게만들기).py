import sys
input = sys.stdin.readline
N, K = map(int, input().split())

num = list(input())

res=K

stack = []

for i in range(N):
    while res and stack:
        if stack[-1] < num[i]:
            stack.pop()
            res-=1
        else:
            break
    stack.append(num[i])

print(''.join(stack[:N-K]))