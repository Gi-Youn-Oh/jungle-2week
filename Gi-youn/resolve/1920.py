import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))

M = int(input())
B_list = list(map(int,input().split()))

A_list.sort() # 이진탐색은 정렬된 리스트에서 가능하다.

# A_list 의 모든 인덱스에 대해서 탐색할 것이기에 start, end 를 A_list의 첫, 끝 인덱스로 지정해준다.
start = 0
end = N-1
def binary_search(i, A_list, start, end):
    if start > end :
        return 0
    mid = (start + end) //2
    if i == A_list[mid]:
        return 1
    elif i < A_list[mid]:
        return binary_search(i, A_list, start, mid -1)
    else :
        return binary_search(i, A_list, mid +1, end)


for i in B_list: # B리스트 인덱스에 대해서 함수를 실행한다. 
    print(binary_search(i, A_list, start, end))
