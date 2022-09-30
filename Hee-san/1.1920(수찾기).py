# # N개의 정수  A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
import sys

N = int(input())

given = list(map(int, sys.stdin.readline().split()))

S = int(input())

check = list(map(int, sys.stdin.readline().split()))

print(given)
print(check)

## 이중 for문 하면 시간초과뜸 

## 이분탐색 or 재귀함수로 풀어보자

