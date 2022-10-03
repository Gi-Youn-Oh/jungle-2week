import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, (-1)*x)

# heappop(), heappush() 함수는 최소힙만 동작하기 때문에 최대힙을 구현하기 위해서는 변형이 필요하다.
# 넣어주는 값에 -1을 곱해 push > 가장큰값이 음수가 되면 가장 작은 값 
# pop 해줄때 -1다시 곱해주면 원래 숫자 출력

# 1258 8 > 최대값이기 때문에 루트에 위치 x > -8 > 가능 > 출력할때 -1* ==8 출력
