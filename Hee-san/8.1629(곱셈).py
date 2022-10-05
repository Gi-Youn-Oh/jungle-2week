

# 10**11 은 10**5 * 10**5 * 10 만들 수 있다.
# 10**5 = 10**2 * 10**2 * 10 으로 만들 수 있다.
# 10**2 = 10**1 * 10**1 로 만들 수 있다.
# 즉 세번의 재귀만으로 답을 구할 수 있다.
# 따라서 b를 계속 반으로 쪼개서 진행시키며 구할 수 있다.

# 주의) 쪼갠 b가 홀수인 경우, 짝수인 경우
# 언제 c로 나눈 나머지를 구할건지
# a 자체가 c보다 클 때 어떻게 할건지
import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())


def find_value(a, b, c):
    if b == 1:
        return a % c
    tmp = find_value(a, b//2, c)
    if b % 2 == 1:
        return tmp**2 * a % c
    else:
        return tmp**2 % c


print(find_value(a, b, c))
