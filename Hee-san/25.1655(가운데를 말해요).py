# 가운데를 하나씩 외칠때마다 동생은 중간값을 말해야한다.
# 총 갯수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다
# 홀수라면 그냥 중간값을 말하면된다.

# ex) 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다
# 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다


import sys
import heapq
input = sys.stdin.readline

N = int(input())

leftHeap = []
rightHeap = []
res = []

# 구하고자 하는 값이 중간값이기 때문에 중간값보다 작은 값들은
# leftHeap에, 큰 값은 rightHeap에 저장하는 방식이다.
# ① 중간값이라는 것은 주어진 N개의 수 중 중간에 위치한 값이기 때문에
# 값을 leftHeap과 rightHeap에 번갈아 넣어줌으로써 두 힙의 균형(개수)을 유지하도록 하여
# leftHeap에서 pop을 했을 때 바로 중간값을 구할 수 있도록 한다.
for _ in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if leftHeap and rightHeap and leftHeap[0] * -1 > rightHeap[0]: # -1을 하는이유는 최소힙 이기 때문에 -를 해줘야 최대 힙 으로 구현 할 수 있다.
        max_value = heapq.heappop(leftHeap)
        min_value = heapq.heappop(rightHeap)
        # 서로서로 값을 교환해준다.
        heapq.heappush(leftHeap, min_value * -1)
        heapq.heappush(rightHeap, max_value * -1)

    print(leftHeap[0] * -1)
    # 다시 출력할 때는 원래대로 되돌려준다.
