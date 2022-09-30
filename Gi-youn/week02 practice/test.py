from ctypes.wintypes import tagRECT


n, m = list(map(int, input().split(' ')))
tree_list = list(map(int, input().split()))

start = 0
end = max(tree_list)

knife_len = 0
while(start <= end):
    total=0
    mid = (start + end) // 2
    for i in tree_list:
        if i > mid :
            total += i-mid
    if total < m :
        end = mid - 1
    else :
        knife_len = mid
        start = mid +1

print(knife_len)










