# 막대기를 일렬로 세운다. 왼쪽부터 차례로 번호를 붙인다.

# 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 즉 , 지금보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다.

# 6, 9, 7, 6, 4, 6


import sys

input = sys.stdin.readline
T = int(input())
stack = []

# stack = [[False] * 5 for _ in range(n)]

for _ in range(T):
    put = int(input().strip())
    stack.append(put)

# 리스트 마지막 인덱스보다 큰값 의 갯수를 카운트해라 (카운트는 시작하는 요소를 포함해야하기 때문에 count는 1부터 시작)
# 여기서 내가 놓친 것 마지막 기둥보다 같은 크기로 큰 2개의기둥이있으면 2개를 카운트해버린다.
# 생각하자 > 오른쪽에서 바라보면 for문을 거꾸로 돌려야하고 계속 최댓값을 꺼내야한다. 

count = 1
last = stack[-1]

for i in reversed(range(T)):
    if stack[i] > last:
        count = count + 1
        last = stack[i]


print(count)
