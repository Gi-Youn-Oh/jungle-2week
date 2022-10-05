import sys

input = sys.stdin.readline

N = int(input())

target_list = list(map(int, input().split()))

M = int(input())

num_list = list(map(int, input().split()))

sorted_list = sorted(target_list)


def findSame(i, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if i == arr[mid]:
            return True
        elif i < arr[mid]:
            end = mid - 1
        elif i > arr[mid]:
            start = mid + 1

        else:
            return False


for i in num_list:
    if findSame(i, sorted_list) == True:
        print(1)
    else:
        print(0)
