# import sys

# input = sys.stdin.readline

# a, b, c = map(int,input().split())

# # print(a,b,c)
# answer = 0
# answer = (a**b) % c

# print(answer)

# 시간초과 > 단축 곱셈의 개수 를 줄이는 분할 정복 
# a = 10 , b = 11 , c = 12
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12

import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,b):
    if b==1:       #b의 값이 1이면 a%c 를 리턴
        return a%c 
    else :
        tmp = multi (a,b //2) # a^(b//2) 를 미리 구한다.
        if b % 2 == 0:
            return (tmp * tmp) % c #b가 짝수인 경우
        else:
            return(tmp * tmp *a) %c # b가 홀수인 경우 

print(multi(a,b))