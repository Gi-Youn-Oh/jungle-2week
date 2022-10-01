n, m = int(input())

list [ 1 2 4 8 9]

start = 1
end =list[-1]-list[0]
distance = 0
def find(start,end,array):
    while start <= end:
        mid = (start+end)//2
        current = list[0]
        count = 1 # 공유기 개수
        for i in range(1,len(list)):
            if list[i] >= current+mid:
                count +=1
                current = list[i]
            if count >= m : #공유기 개수가 설정한 m개이상
                global distance
                start = mid +1
                distance = mid
            else :
                end = mid - 1

print()


