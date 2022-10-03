import sys
input = sys.stdin.readline

N = int(input())

arr = []
_sum = []

for i in range(N):
    arr.append(int(input()))

for i in arr:
    if i == 0 :
        _sum.pop()
        # if len(_sum) == 0:
        #     print(-1)
    else :
        _sum.append(i)    


print(sum(_sum))