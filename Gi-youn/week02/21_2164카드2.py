import sys
from collections import deque

input = sys.stdin. readline

N= int(input())

arr = deque([])
for i in range(1,N+1):
    arr.append(i)

# print(arr)

while (len(arr)>1):
    arr.popleft()
    move_num = arr.popleft()
    arr.append(move_num)

print(arr[0])