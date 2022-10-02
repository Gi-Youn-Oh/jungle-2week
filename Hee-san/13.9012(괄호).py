# 괄호 문자열 (PS) ( , ) 만으로 구성되어있음
# 올바른 구성의 괄호문자열을 VPS 라고함
# 한쌍 "()" 괄호문자열을 기본VPS 라고 부른다.

# 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES, NO 로 나타내라

from distutils.cmd import Command
import sys

input = sys.stdin.readline
T = int(input())

# 입력 받을 떄마다 배열에 저장해야 함
# 빈 배열이 필요하다

for _ in range(T):
    def find():
        stack = []
        command = input().strip()
        for i in command:
            if i == "(":
                stack.append(i)

            elif i == ")":
                if len(stack) == 0:
                    return print('NO')
                else:
                    stack.pop()
        if len(stack) == 0:
            print("YES")
        else:
            print('NO')

    find()
