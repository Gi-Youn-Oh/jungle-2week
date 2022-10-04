# 완전 탐색 시간초과
# stack


N = int(input())  # 탑의 개수
top_list = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top_list[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))


# 6, 9, 5, 7, 4를 예로 들면 수행 과정은 다음과 같다.

# stack = [ ]  -> 최댓값을 저장할 스택
# answer = [ ] -> 수신 탑 인덱스 저장

# 1. 처음 스택은 비어있기 때문에 최댓값이 0인 상황이다. 따라서 6을 수신할 수 있는 탑이 존재하지 않기 때문에 answer에 0을 삽입하고, stack에는 인덱스와 6의 값을 삽입한다. 

# stack = [[0, 6]]
# answer = [0]
 
# 2. 9와 stack의 top(6)과 비교하면 9가 더 크기 때문에 stack에서 pop을 진행한다. pop을 진행한 후 stack은 비어있게 되며 수신할 탑이 없다는 의미를 나타낸다. 따라서 answer에 0을 삽입한다. stack에는 추가된 [1, 9]만 남게 된다.

# stack = [[1, 9]]
# answer = [0, 0]

# 3. 5는 stack의 top(9) 보다 작기 때문에 수신 가능한 탑이 존재하는 상황이다. 따라서 stack의 top에서 index를 가져와서 answer에 대입한다. (대입하는 과정에서 1을 더해줘야 한다!)

# stack = [[1, 9], [2, 5]]
# answer = [0, 0, 2]

# 4. 7은 stack의 top(5)과 비교하면 7이 더 크기 때문에 stack에서 pop을 진행한다. 그 후 stack의 top(9)보다 작기 때문에 수신 가능한 상황이다. 따라서 answer에는 stack의 top에서 가져온 인덱스를 추가한다.

# stack = [[1, 9], [3, 7]]
# answer = [0, 0, 2, 2]

# 5. 5는 stack의 top(7)보다 작기 때문에 수신 가능한 탑이 존재하는 상황이다. 따라서 stack의 top에서 index를 가져와서 answer에 대입한다. 

# stack[[1, 9], [3, 7], [4, 4]]
# anwer = [0, 0, 2, 2, 4]