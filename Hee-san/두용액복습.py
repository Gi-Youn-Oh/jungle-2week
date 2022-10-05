import sys

input = sys.stdin.readline

N = int(input().rstrip())

water = list(map(int, input().split()))
water.sort()
# 처음에 정렬된 배열 젤 작은값(왼쪽) 과 큰값(오른쪽)의 인덱스를 가리키는 변수를 만든다.
left, right = 0, N-1
idxl = 0
idxr = 0
sum_value = 0
min_value = sys.maxsize

while left < right:
    sum_value = water[left] + water[right]
    if min_value > abs(sum_value):
        idxl = left
        idxr = right
        min_value = abs(sum_value)
    if sum_value < 0: # sum이 음수가 나온다는 것은 left가 더 크다는 것이므로 0에가까워지려면 오른쪽으로 한칸 옮겨줘야한다.
        left = left + 1
    elif sum_value > 0:# sum이 양수가 나온다는 것은 right가 더 크다는 것이므로 0에가까워지려면 왼쪽으로 한칸 옮겨줘야한다.
        right = right - 1
    else:
        break

print(water[idxl],water[idxr])


# 리스트의 모든 원소에 대해서 각 핪을 구해보고, 
# 절대값으로 가장 작은 수를 찾는다 (0에가장 가까운 수)
# 과정을 빠르게 하기위해 이분탐색을 사용
# 답 도출 > 원소 두개 (합이 0에 제일 가까운 수)

# 더하는 과정을 반복문으로 만들기
# 최소값을 구하기 위해 최데값 변수를 하나 선정
# 두 인자를 더한값이 최대값 변수와 비교하여 최소값이 리셋 되도록 설정
# 그때의 두 인자 값을 return