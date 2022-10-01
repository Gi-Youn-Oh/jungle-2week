import sys
T = int(input())
stack = []  # 재할당 개념 공부

# stack = [[False] * 5 for _ in range(n)]

for _ in range(T):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(int(command[1]))

    if command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            pop_list = stack.pop()
            print(pop_list)

    if command[0] == "size":
        print(len(stack))

    if command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack[-1]))

    if command[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)
