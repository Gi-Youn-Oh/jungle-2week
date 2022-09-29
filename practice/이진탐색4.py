#파라메트릭 서치 = 최적화 문제를 결정문제 (예, 아니오)로 바꾸어 해결하는 기법
#  ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있습니다. 

#  어떤 요소에 따라 변할 수 있는 것을 찾는다 >> 변수가 됨.
#  그 변수의 범위를 좁혀나가며 찾느다. , 탐색범위가 클 때 이진탐색을 떠올린다.

# 떡의 개수 (N) 와 요청한 떡의 길이 (M) 입력
from re import S
from unittest import result


n, m = list(map(int, input().split(' ')))

# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적) #H가 높아지면 가져가는 떡길이가 낮아지고 H가 낮아지면 가져가는 떡 길이가 길어진다.
result = 0
while(start <= end):
    total = 0    # 손님이 가져갈 떡볶이 길이
    mid = (start + end) // 2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x-mid
        #떡의 양이 부족할 경우 더 많이 자르기 (왼쪽부분 탐색)
    if total < m :
        end = mid -1
    #떡의 양이 충분할 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답출력
print(result)

