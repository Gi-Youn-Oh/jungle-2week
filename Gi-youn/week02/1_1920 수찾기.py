#이진탐색

from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))  # 이진탐색은 정렬된 배열에 대해서 실행가능 
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:  # 수가 0보다 작다면 실행할 필요 x
        return 0
    m = (start+end)//2  # 중간값을 a리스트의 중간으로 설정 / a리스트에 대해서 b리스트 인덱스를 확인
    if l == N[m]:           # b리스트의 인덱스가 a리스트의 중간 인덱스 와 같다면 
        return 1
    elif l < N[m]:              # b리스트의 인덱스가  a리스트의 인덱스보다 작다면 
        return binary(l, N, start, m-1) # 왼쪽으로 즉 작은쪽으로 범위 좁히기
    else:
        return binary(l, N, m+1, end) # b리스트의 인덱스가 a리스트의 인덱스보다 크다면 출발점을 높힌다.
            
for l in M:             #b리스트의 인덱스에 대해서
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))

#집합자료형

from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

