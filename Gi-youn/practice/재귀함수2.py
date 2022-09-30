메모 = { 1:1, 2:1 }  #dictionary

def f(n):
    if n in 메모 :
        return 메모[n]  # 메모 딕셔너리 안에 값이 있다면 리턴
    else:            # 없다면
        output = f(n-1) + (n-2) # 값 생성
        메모[n] = output         # 메모에 추가
        return  output              

# 결과적으로 메모 딕셔너리에 데이터가 쌓이게 되고 쌓인 데이터를 출력만 해주면 된다.


# 조기리턴
def f(n):
    if n in 메모 :
        return 메모[n]  # 메모 딕셔너리 안에 값이 있다면 리턴  
    output = f(n-1) + (n-2) # 값 생성
    메모[n] = output         # 메모에 추가
    return  output              