import sys
input = sys.stdin.readline

N, L = map(int, input().split())
levels = []
for i in range(N):
    levels.append(int(input()))

levels.sort()

start = min(levels)
end = start + L

res = 0
while (start <= end) :
    mid = (start + end) // 2
    
    gap = 0
    for i in levels:
        if mid > i:
            gap += (mid - i)
    
    if gap < L :
        start = mid + 1 
        res = max(mid,res)
    else : 
        end = mid - 1

        