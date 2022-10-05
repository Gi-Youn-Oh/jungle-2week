# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
# 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

import sys


input = sys.stdin.readline

n = int(input())  # 5

water = list(map(int, input().split()))  # [-2, 4, -99, -1, -98]

water.sort()  # 이진탐색 하기 위해 오름차순 으로 정렬 해준다
left, right = 0, n-1  # 제일 작은 수 즉 arr list의 첫번째 인덱스  / 제일 큰 수 인덱스의 가장 마지막 인덱스
idxL, idxR = 0, 0  # 변수로두고 교체해주기
_sum = 0
_min = sys.maxsize  # 최소값을 가장큰값으로 두어서 비교할 대상을 만들어준다.

while left < right:
    _sum = water[left] + water[right]
    if _min > abs(_sum): # 0에 가장 가까운 값을 찾는 것이므로 절대값(0까지의 거리) 처리를 해준다.
        idxL = left
        idxR = right
        _min = abs(_sum)
    if _sum < 0:  # sum이 음수가 나온다는 것은 left가 더 크다는 것이므로 0에가까워지려면 오른쪽으로 한칸 옮겨줘야한다.
        left += 1
    elif _sum > 0:  # sum이 양수가 나온다는 것은 right가 더 크다는 것이므로 0에가까워지려면 왼쪽으로 한칸 옮겨줘야한다.
        right -= 1
    # 0 인 경우
    else:
        break

print(water[idxL], water[idxR])
