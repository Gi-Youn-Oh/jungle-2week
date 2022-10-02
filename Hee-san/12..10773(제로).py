

# if call wrong number, 재현 talk '0' and then 재민 remove the it
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
# 첫째 줄에 정수 k >> 1 <= K <=100,000


import sys

input = sys.stdin.readline
K = int(input())

# 입력 받을 떄마다 배열에 저장해야 함
# 빈 배열이 필요하다

stack = []
for _ in range(K):
    command = int(input())
    if command == 0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))
