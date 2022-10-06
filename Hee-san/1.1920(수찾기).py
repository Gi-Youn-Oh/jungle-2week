# N개의 정수  A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
# N개의 정수  A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.


import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

k = int(input())

target_list = list(map(int, input().split()))

sortedNumList = sorted(num_list)

# sortedNumList = [1,2,3,4,5]



# while else 문 사용
def findSame(sortedNumList):
    for i in target_list:
        start = 0
        end = len(sortedNumList) - 1
        while start <= end:
            mid = (start + end) // 2
            if i == sortedNumList[mid]:
                # i == mid 가 아니라 i = sortedNumList[mid] (인덱스로 접근해야함)
                print(1)
                break
            elif i < sortedNumList[mid]:
                end = mid - 1  # 얘는 숫자임
            elif i > sortedNumList[mid]:
                start = mid + 1  # 얘는 숫자임
        else:
            print(0)


findSame(sortedNumList)


# for 문 안에 함수를 넣어서 함수를 반복 실행한다. 
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_arr = list(map(int, input().split()))
# m = int(input())
# m_arr = list(map(int, input().split()))
# n_arr.sort() #[1,2,3,4,5]

# def binary(i):
#     start = 0
#     end = n - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if n_arr[mid] == i:
#             return True
#         if i < n_arr[mid]:
#             end = mid - 1
#         elif i > n_arr[mid]:
#             start = mid + 1


# for i in range(m):
#     if binary(m_arr[i]):
#         print(1)
#     else:
#         print(0)
