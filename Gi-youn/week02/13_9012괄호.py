import sys
input = sys.stdin.readline

#입력 데이터 수를 입력받는다.
num = int(input())

#for문 안에서 사용할 stack 리스트 생성
stack = []
for i in range(num) :
    #문자열 하나씩 끊어서 입력받기 #((()) 입력 시 ['(', '(', '(', ')', ')'] 로 입력된다.
    arr = list(input().rstrip())


    #arr for문 돌리며 '('일때 stack에 담기
    for j in range(len(arr)) :
        if arr[j] == '(' :
            stack.append(arr[j]) #stack에 push해준다.
        else : #')'일때는 pop하기
            if not stack : #stack이 비어있으면
                print('NO')
                break #안쪽 for~else문을 모두 빠져나옴
            stack.pop() #stack에서 pop()
    else : #for문을 모두 돌고 나왔는 데 stack이 empty면 'YES'를 출력 그렇지 않으면 'NO'를 출력
        if not stack : #비어있으면
            print('YES')
        else :
            print('NO')


    #스택을 비워준다.
    stack=[]