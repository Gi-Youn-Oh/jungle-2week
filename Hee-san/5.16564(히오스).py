import sys
# 첫째 줄에는 캐릭터의 개수 N, 올릴 수 있는 레벨 총합 K가 주어진다
input = sys.stdin.readline
N, K = map(int, input().split())

levels = sorted([int(input()) for _ in range(N)])

start = min(levels)
end = start + K

res = 0
while start <= end:
    mid = (start + end) // 2
    hap = 0
    for level in levels:
        if mid > level:
            hap = hap + (mid-level)
    if hap <= K:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1
print(res)
