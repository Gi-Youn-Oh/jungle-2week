import sys


input = sys.stdin.readline

N, C = map(int, input().split())

house = []
for _ in range(N):
    num = int(input())
    house.append(num)
# 먼저 이진탐색을 하려면 전제조건이 그 배열이 정렬된 배열 이기 때문에 정렬을 해준다

sorted_house = sorted(house)
print(sorted_house)
# 처음 집에서 그다음 탐색하려는 집의 간격을 이용해서 이진 탐색을 한다.

# 항상 잊지 말아야 할 것!
# 계속 값이 바뀌어서 실행되어야 하는 변수는 while문 안에 작성 한다는 것이다.


# 함수로 작성해보자

def install_wifi(start, end, array):
    while start <= end:
        mid = (start + end) // 2
        just_installed = array[0]
        count = 1  # 처음의 집에 공유기 한개가 설치되어있으므로.

        for i in range(1, len(array)):
            if array[i] >= just_installed + mid:
                count = count + 1
                just_installed = array[i]  # 추가 설치된 곳이 다시 기준이 된다.

        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = sorted_house[-1] - sorted_house[0]
answer = 0

install_wifi(start, end, sorted_house)
print(answer)
