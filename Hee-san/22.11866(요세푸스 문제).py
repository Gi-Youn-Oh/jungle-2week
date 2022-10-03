# 원에서 사람들이 제거되는 순서를  (N,K)-요세푸스 순열이라고 한다.
# ex (7,3) - 요세푸스 순열은 <3,6,2,7,5,1,4> 이다

import sys
from collections import deque

num_list = deque()
answer = []
input = sys.stdin.readline

N, K = map(int, input().split())

for i in range(1, N+1):
    num_list.append(i)

print(num_list) #[1,2,3,4,5,6,7]
print(answer)

while num_list:
    for i in range(K-1): 
        num_list.append(num_list.popleft())

    answer.append(num_list.popleft())


print("<", end="")
for i in range(len(answer)-1):
    print("%d, " % answer[i], end='')
print(answer[-1], end='')
print(">")
