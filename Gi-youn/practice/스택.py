# 스택은 제일 마지막에 들어간 값을 제일 먼저 뽑는다. First in last out / last in first out 
# 큐는 제일 먼저 들어간 값을 제일먼저 뽑는다. First in first out

class stack1:
    def __init__(self, size=10000):
        self.arr = [None] * size
        self.last_index = 0 # 현재 사용할 수 있덱스
    def push(self,value):
        # self. arr = [ None, None, None,...]
        # self.last_index = 0
        self.arr[self.last_index] = value
        self.last_index += 1
    def pop(self):
        # 뒤에서 뽑기
        # last_index = 0 >> -1
        if self.empty():
            raise Exception('stack is empty')
        self.last_index = self.last_index -1
        return self.arr[self.last_index]

    def empty(self):
        if self.last_index == 0:
            return True
        else :
            return False
    
    def peek(self):
        if self.empty():
            raise Exception('stack is empty')
        return self.arr[self.last_index -1]

st =stack1(100)
print(st.empty())
print(st.peek())

# print(len(st.arr))
# print(st.arr)
# print(st.last_index)
# st.push(10)
# print(st.arr)
# print(st.last_index)
# st.push(20)
# print(st.arr)
# print(st.last_index)

# print('pop', st.pop())