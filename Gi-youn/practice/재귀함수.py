#재귀함수 마스터하기
#Pactorial
# n! = 1*2*3*(n-1)(n)

def factorial_1(n):
    변수 = 1
    for i in range(1, n+1):
        변수 *= i
    return 변수


# 0! =1    
# n! = n*(n-1)
def factorial_2(n):
    if n == 0 :
        return 1
    else :
        return n*factorial_2(n-1)    

print(factorial_1(10))
print(factorial_2(10))


