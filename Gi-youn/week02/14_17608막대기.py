import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    stack.append(int(input()))

# print(stack)

Max = stack[-1]
result = 1
for  i in range(len(stack)-1, -1 , -1):  #인덱스 마지막 부터 0번쨰 까지 역순으로
    if stack[i] > Max :
        result +=1
        Max = stack[i]

print(result)

