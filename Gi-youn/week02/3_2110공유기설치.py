import sys
from turtle import home
input = sys.stdin.readline

N, C = map(int, input().split())
home_list = []
for i in range(N):
    home_list.append(int(input()))

home_list.sort()

start = 1
end = home_list[-1] - home_list[0]
answer = 0

def binary_search(home_list, start, end):
    while (start <= end):
        mid = (start + end) // 2
        count =1
        current = home_list[0]
        for i in range(1, len(home_list)):
            if home_list[i] >= current + mid :
                count +=1
                current = home_list[i]
        if count < C :
            end = mid - 1
        else :
            start = mid + 1
            global answer
            answer = mid

binary_search(home_list, start, end )
print(answer)