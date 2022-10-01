from calendar import c
from re import L

class stack:
    def __init__(self):
        self.data = []
    # 데이터 비어있는지 확인
    def is_empty(self):
        return len(self.data) == 0
    # 데이터 넣기
    def push(self, item):
        self.data.append(item) 
    # 데이터 뽑기 / 원본 삭제
    def pop(self):
        return self.data.pop()
    # 데이터 복사 / 원본 유지
    def peek(self):
        return self.data[-1]

# 중위 표현식 > 후위 표현식

# a+b*c > 순서 인식못함

# ab*c+

# ( a+b ) * c
# 여는 괄호 ( 무조건 스택에 넣고 닫는 괄호를 만나게 되면 여는괄호를 만날때까지 뽑아오고 두 괄호를 삭제

# ab+ C *

priority = { '*' : 3, '/' : 3,
             '+' : 2, '-' : 2,
             '(' : 1}

expr = []
operator = stack()
result = []
tmp = input("식을 입력하세요: ")

for i in tmp:
    if i == ' ':
        expr.append(i)

for i in expr:
    if i == '(':
        operator.push(i)

    elif i in '+-*/' :
        if operator.is_empty():
            operator.push(i)
        else:
            if priority[operator.peek()] >= priority[i]:
                result.append(operator.pop())
                operator.push(i)
            else:
                operator.push(i)
    elif i == ')':
        while True:
            tmp = operator.pop()
            if tmp == '(':
                break
            result.append(tmp)

    else:
        result.append(i)

while not(operator.is_empty()):
    result.append(operator.pop())


print('',join(result))