import sys
n = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
B_list = list(map(int,sys.stdin.readline().split()))

# print(A_list)
# print(B_list)
# C_list = [] 
# print(B_list[0:m])
for i in A_list:
    if i == B_list[0:m]:
        print(1)
    else :
        print(0)
       
# print(C_list, sep = '\n')


# 재귀로 만들기
# def find(digit_number):
#     result = []
#     for i in B_list:
#         for j in A_list:
#             if j == i :
#                 return 1
#             else :
#                 return 0

# 이진탐색 방법 찾기