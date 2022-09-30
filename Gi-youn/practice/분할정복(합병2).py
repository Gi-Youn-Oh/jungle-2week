# 합병 정렬 inhance 
    # 전체를 다 나누고 하나씩 정렬이 아닌 나누어진 그 리스트 안에서 우선 정렬후 합친다. 

# def mergesort2 (S, low, high):
#     if (low < high):
#         mid = (low + high) // 2
#         mergesort2(S, low, mid)
#         mergesort2(S, mid +1, high)
#         merge2(S, low, mid, high)


def merge2 (S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while (i <= mid and j <= high): # U 리스트안에서 자체 정렬
        if (S[i] < S[j]):
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1 
    if (i <= mid):
        U += S[i : mid + 1]
    else:
        U += S[j : high +1]
    for k in range(low, high +1 ):
        S[k] = U[k-low]  
