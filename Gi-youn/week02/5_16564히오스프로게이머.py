import sys

input = sys.stdin.readline

N, k = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

# print(arr)
arr.sort()
start = min(arr)
end = start + k 

res = 0
while (start <= end) :
    mid = (start+end) // 2
    
    gap = 0
    for i in arr:
        if mid > i :
          gap += (mid - i)

    if gap <= k:
        start = mid +1 
        res = max(mid,res)
    else:
        end = mid -1

print(res) 
    
