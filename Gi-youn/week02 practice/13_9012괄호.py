import sys
input = sys.stdin.readline

T = int(input())

stack = [] # 받을 한줄 당 새롭게 스택
for i in range(T): # T개수 만큼 스택한줄씩 받는다.
    arr = list(input().rstrip()) # 한줄을 받는다.

    for j in range(len(arr)): # 받은 한줄에 대해서 (로 시작하면 stack에 추가
        if arr[j] == '(':
            stack.append(arr[j])
        else :                  
            if not stack:           # 스택이 비어있으면 no 즉 (로 시작하지 않으면 애초에 성립이 안된다. 
                print('NO')
                break
            else:
                stack.pop()     # 들어있으면 pop 빼준다 . ( ) 짝이 맞다 
    else:               # for,else while,else 의 활용
        if not stack:    # 비어있으면  ( ) 짝맞게 순서대로 들어왔으니까 yes
            print('YES') 
        else :
            print('NO')     # 들어있으면 () ( 짝이 안맞으므로 no 

    stack=[] # 한줄 확인 끝나면 다시 받기위해서 비워준다.

# 경우의 수
# () > yes
# () ( > no
# ) > no 
# arr = []
# open = '('
# close = ')'
# set = open+close
# for i in range(T):
#     arr(input())
# # print(arr)
#     if arr[i] == len(open) == len(close):
#         print('YES')
#     else :
#         print("NO")
