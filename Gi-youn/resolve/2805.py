import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))
# print (N, M)
tree_list = list(map(int, input().split()))
# print(tree_list)
tree_list.sort()

start = 0 #나무 최저길이
end = max(tree_list) #나무 최대길이
res = 0 #톱의 최대길이 (추후 변경)

while (start <= end) :
    total = 0 #가져갈 나무의 길이
    mid = (start + end) // 2
    for i in tree_list:
        if i > mid :
            total += (i-mid)
    if total < M :
        end = mid - 1
    else :
        start = mid + 1
        res = mid
print(res)

# 부족한점 
end = 20으로 한정함 / max(tree_list) 로 새로운 값에도 변경적용되게
total = 0 리셋에대한 구조적 생각
자르는 조건 > 나무의 길이i가 톱길이mid보다 클때