from ast import Import
import sys
import heapq
input = sys.stdin.readline
N = int(input())

# 최대힙을 구현만 하면 되는 문제이다.
heap = []  # 비어있는 배열에서 시작한다.
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
            # 최대힙을 최소힙 구현에서 입력되는 수들에 -1만
            # 곱해주는 방식으로 간단하게 구현할 수 있다.
    else:
        heapq.heappush(heap, x*(-1))

# import sys
# input = sys.stdin.readline
# import heapq

# N = int(input())
# heap = []
# for _ in range(N):
#     x = int(input())
#     if x == 0:  # 0을 입력받으면 배열에서 최댓값을 출력하고 그 값을 제거해라.
#         if len(heap) == 0:
#             print(0)
#         else:
#             print((-1)*heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, (-1)*x)
