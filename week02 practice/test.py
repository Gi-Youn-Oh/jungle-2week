import sys
n = int(sys.stdin.readline())
A_list = set(map(sys.stdin.readline().split()))

m = int(sys.stdin.readline())
B_list = list(map(int,sys.stdin.readline().split()))
 
 
for i in B_list:
    for j in A_list:
        if j == i :
            print(1) 
        else :
            print(0) 