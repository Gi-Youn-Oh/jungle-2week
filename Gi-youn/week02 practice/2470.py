import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

left, right = 0, N-1 # start, end 
idxL, idxR = 0, 0
_sum = 0 # mid 
_min =sys.maxsize

while (left < right):
    _sum = num_list[left] + num_list[right]
    if _min > abs(_sum):
        idxL = left
        idxR = right 
        _min = abs(_sum)
    if _sum < 0:
        left += 1
    elif _sum > 0:
        right -= 1
    else :
        break

print(num_list[idxL], num_list[idxR])

# start end 의 자유로운 응용
# 최소값을 구할때 임의의 최대값을 설정해두고 리턴 