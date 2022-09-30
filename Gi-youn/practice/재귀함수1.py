#피보나치 수열 

# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)
# # f(3) = f(2) + f(1) = 2
# # f(4) = f(3) + f(2) = 3
# #5
# #8
# #13
counter = 0

def f(n):
    global counter # 함수 밖에 정의 되어있는 변수를 사용할 때 global
    counter += 1
    if n==1 or n==2:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(1))
print(f(2))            
print(f(3))
print(f(4))
print(f(5))

print(f(40))