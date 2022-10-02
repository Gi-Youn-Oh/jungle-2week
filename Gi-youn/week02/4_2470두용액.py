import sys
input = sys.stdin.readline

N = int(input().rstrip()) # rstrip() > 다음 열로 
arr = list(map(int, input().split()))
arr.sort() # 작은 수 부터 최대 수까지

left, right = 0, N-1 # 제일 작은 수 즉 arr list의 첫번째 인덱스  / 제일 큰 수 인덱스의 가장 마지막 인덱스
idxL, idxR =0,0  #변수로두고 교체해주기
_sum = 0 
_min = sys.maxsize

while left < right:
    _sum = arr[left] + arr[right]
    if _min > abs(_sum):
        idxL = left
        idxRE = right
        _min = abs(_sum)
    if _sum <0 :
        left+=1
    elif _sum >0:
        right -=1
    #0 인 경우
    else:
        break

print(arr[idxL], arr[idxR])



# 리스트의 모든 원소에 대해서 각 핪을 구해보고, 
# 절대값으로 가장 작은 수를 찾는다 (0에가장 가까운 수)
# 과정을 빠르게 하기위해 이분탐색을 사용
# 답 도출 > 원소 두개 (합이 0에 제일 가까운 수)

# 더하는 과정을 반복문으로 만들기
# 최소값을 구하기 위해 최데값 변수를 하나 선정
# 두 인자를 더한값이 최대값 변수와 비교하여 최소값이 리셋 되도록 설정
# 그때의 두 인자 값을 return


import sys

N = int(sys.stdin.readline())

water_list = []

for i in range(N):
    water_list.append(i)
start = water_list[0]
end = water_list[-1]

sum = 10e9

first, second = map(int(sys.stdin.readline()))

def sum_two(start, mid, end):
    while (start <= end):
        mid = (start + end) // 2
        for i in water_list[1:]:
            new = start + i 
            if new < sum :
                start = first, i = second
            else:
                find(answer)
        if abs(new) < abs():
            answer = (first,second)

print()  

