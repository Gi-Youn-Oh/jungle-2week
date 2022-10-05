# 첫째 줄에 탑의 수를 나타내는 정수 N이 주어짐 , N은 1이상 500,000이하다
# 둘째줄에 하나의 빈칸을 두고 탑들의 높이가 직선상에 놓인 순서대로 주어짐. 탑들의 높이는 1이상 100,000,000이다.

# 예제 입력 1 
# 5
# 6 9 5 7 4

# 예제 출력 1 
# 0 0 2 2 4
# 현재 탑이 쏜 레이저를 수신한 탑의 인덱스를 구하라. 나보다 높은 탑이 나의 다음 인덱스면 수신호는 0 이다.
import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))


stack = []
res = [0 for i in range(N)]

for i in range(N): # 0 - 1 - 2 - 3 - 4
    while stack:
        if stack[-1][1] > top[i]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i,top[i]]) # 처음 [[0,6]]

print(*res)