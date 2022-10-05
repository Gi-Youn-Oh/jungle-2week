import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 0, max(trees)
while start <= end:
    mid = (start+end)//2  # 중간 위치  mid가 톱날의 길이를 의미한다.
    gain = 0
    # 나무 자르기
    for tree in trees:
        # 나무의 높이가 절단기 높이보다 크다면
        if tree > mid:
            gain = gain + (tree-mid)
    # 자른 나무들의 길이가 목표값 이상이라면
    if gain == M:
        print(mid)
        break

    elif gain > M:
        # 시작점 조정
        start = mid + 1  # 11 15 20
    else:
        # 끝점 조정

        end = mid - 1
else:
    print(end)

