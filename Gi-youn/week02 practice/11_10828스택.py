import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    word = sys.stdin.readline().split() # 입력받는데 split해서 입력 받기
    order = word[0] #명령어 받기

    if order == 'push':
        value = word[1]
        stack.append(value)
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif order == 'top' :
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.peek())
