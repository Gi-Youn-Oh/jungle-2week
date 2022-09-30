# 5 3
# 1
# 2
# 8
# 4
# 9


n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1
        for i in range(1, len(array)):
            if array[i] >= current + mid: 
                count += 1 # 공유기 1대를 추가설치해라.
                current = array[i] # 설치된곳을 기준으로 다시 설치할 곳을 본다.
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1 # end 가 3임(처음 들림.)
start = 1
end = array[-1] - array[0]
answer = 0
binary_search(array, start, end)
print(answer)

