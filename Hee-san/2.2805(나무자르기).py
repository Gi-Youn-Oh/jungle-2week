# 나무 M미터 필요하다.
# 절단기에 높이 H를 지정해야 한다.
# 높이를 지정하면 톱날이 땅으로부터 H미터 올라간다.
# 그 다음, 한줄에 나란히 서있는 나무들을 모두 절단 해버린다.
# H보다 큰 나무들은 H 위에 부분이 잘릴 것이고 낮은 나무는 잘리지 않을 것이다.
# ex_  H가 15이면 자른 뒤는 [20,15,10,17] --> [15,15,10,15]가 된다.
# 상근이가 들고가는 나무는 [5,0,0,2] 가 된다. 5m ,2m 나무 2개> 총 7m 들고감.
# 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.


# 적어도 M미터의 나무를 가져가려면 절단기의 높이(H)가 얼마가 되어야 하는지에 대한 프로그램을 작성하시오.

# 4(나무 갯수) 7(최소로 가지고갈 나무길이)
# 20 15 10 17

import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)
while start <= end:
    mid = (start+end)//2  # 중간 위치  mid가 톱날의 길이를 의미한다.
    gain = 0
    # 나무 자르기
    for tree in trees:
        # 나무의 높이가 절단기 높이보다 크다면
        if tree > mid:
            gain = gain + (tree-mid)
    # 자른 나무들의 길이가 목표값 이상이라면
    if gain >= M:
        # 시작점 조정
        start = mid + 1
    else:
        # 끝점 조정

        end = mid - 1

# 답출력
print(end)

# 그림으로 생각해보도록 노력하자. 어떻게 진행이되는지.
