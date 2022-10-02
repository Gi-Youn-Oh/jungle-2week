# N개의 정수  A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort() #[1,2,3,4,5]

def binary(i):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == i:
            return True
        if i < n_arr[mid]:
            end = mid - 1
        elif i > n_arr[mid]:
            start = mid + 1


for i in range(m):
    if binary(m_arr[i]):
        print(1)
    else:
        print(0)

# 풀이

# 이분 탐색 알고리즘에 따라서 데이터가 포함되어 있는지 확인하는 풀이 방법을 사용했습니다.
# 이분 탐색을 위해서 집합 N을 먼저 정렬시켰습니다.
# 시작과 끝 지점의 index를 지정합니다.
# 시작 인덱스와 끝 인덱스를 사용해서 중간 지점의 인덱스를 구합니다.
# 중간 지점의 값과 element를 비교합니다.
# 동일한 값이면 찾았다!
# 값이 크다 => 중간보다 윗부분에서 탐색
# 값이 작다 => 중간보다 작은 부분에서 탐색
# 위 과정을 확인할 리스트가 없을 때까지 계속해서 반복한다.
# 전체 리스트에서 확인이 불가능하면 없는 것으로 판별
