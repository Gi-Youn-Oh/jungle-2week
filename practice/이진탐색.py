# 이진탐색 : 정렬되어 있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 이진탐색은 시작점 끝점 중간점을 이용하여 탐색범위를 설정합니다.

# 이진탐색 소스코드 구현 (재귀함수)
from unittest import result


def binary_search(array, target, start, end): # 배열, 찾고자하는것, 출발점 ,끝점 
    if start > end: # 시작점이 끝점보다 크다면 존재할수 없다.
        return None
    mid = (start + end ) // 2  #중간점 명시
    if array[mid] == target: # 찾은경우 중간점 인덱스 반환
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1) # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else:
        return binary_search(array, target, mid + 1, end) # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    
n, target = list(map(int, input().split())) #원소의 개수와 찾고자 하는 값 받기

array = list(map(int, input().split())) #전체 원소 입력받기

# 결과출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else: 
    print(result + 1)     #  인덱스는 0부터 시작하므로 +1 

