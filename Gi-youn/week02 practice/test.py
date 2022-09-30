# from re import S
# from unittest import result

# 나무의수 n, 나무의길이 m
n, m = list(map(int, input().split(' ')))

# 각 나무의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

mid_mid = len(array)//2
left_arr = array[:mid_mid]
right_arr = array[mid_mid:]
# print(left_arr, right_arr)
# 이진 탐색 수행 (반복적) #H가 높아지면 가져가는 나무의 길이가 낮아지고 H가 낮아지면 가져가는 나무의 길이가 길어진다.
result = 0
def half_half(left_arr, right_arr):
    while(start <= end):
        total = 0    # 가져갈 나무의길이
        mid = (start + end) // 2
        for x in array:
            #잘랐을 때의 나무길이의 총합 계산
            if x > mid:
                total += x - mid
            #나무길이가 부족할 경우 더 많이 자르기 (왼쪽부분 탐색)
        if total < m :
            end = mid -1
        #나무길이가 충분 충분할 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1

array = (left_arr+right_arr)
# 정답출력
print(half_half(array))