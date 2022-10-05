# 5 3
# 1
# 2
# 8
# 4
# 9

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()


start = 1
end = house[-1] - house[0]  # 마지막 집과 첫집의 간격을 end값으로 한다.
answer = 0  # 설치되는 공유기 갯수


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        just_installed = array[0]  # 처음 설치되어있는 첫번째 집
        count = 1  # 1개가 설치된 상태에서 시작하니까 count 를 1로 놓고 시작
        
        for i in range(1, len(array)):
            if array[i] >= just_installed + mid:
                count += 1  # 공유기 1대를 추가설치해라.
                just_installed = array[i]  # 설치된곳을 기준으로 다시 설치할 곳을 본다.
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


binary_search(house, start, end)
print(answer)