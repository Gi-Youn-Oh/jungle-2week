def mergesort (S):
    n = len(S)
    if (n <= 1):
        return S
    else :
        mid = n // 2
        U = mergesort(S[0: mid])
        V = mergesort(S[mid:n])
        return merge(U,V)

def merge(U,V):
    S = []
    i = j = 0
    while (i <len(U) and j <len(V)): # 두 정렬의 인덱스 값을 비교하여 새로운 S 리스트에 순서대로 정렬
        if (U[i] <V[j]):
            S.append(U[i])
            i += 1
        else :
            S.append(V[j])
            j += 1
    # U리스트나 V 리스트중 남은 리스트의 숫자들을 새로운 정렬 리스트 S 에 추가정렬 해준다.        
    if (i < len(U)):
        S += U[i : len(U)]
    else :
        S += V[j : len(V)]
    return S

    # S = [ 27, 10 ,12, 20, 25, 13, 15, 22]
    # print('Before: ', S)
    # X = mergesort(S)
    # print(' After: ', X)
