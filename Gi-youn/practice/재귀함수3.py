# 코드가 복잡할때는 작은 것부터 큰것으로 하나씩 단계별로 이해해나가면 수월하다.
# 디버깅도 활용 작섣후에
 # list + list
 # [] + [ 1, 2, 3] = [1, 2, 3]

def flatten(data):  
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else :
            # output.append(item)
            output +=[item]         # [] + [1], [1] + [2] +[1,2] + [3] , [1, 2, 3], 
    return output

# 함수를 짜고 이해할 때 반복문의 구조를 파악하고, 변수 (output) 즉, return 값이 어떻게 변화하는지 파악한다. 
# 구조를 덩어리로 보면 이해가 편하다. 
# 이 구조에서는 example 의 데이터를 for 문에서 리스트를 벗겨주고, else 문에서 output으로 리스트를 새롭게 추가해서 1차원 리스트로 반환한다.  

example = [ [1,2,3], [4,[5,6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))