from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if self.empty():
            raise Exception("empty queue")
        
        return self.dq.popleft()

    def size(self):
        return len(self.dq)

    def empty(self):
        return int(not self.dq)

    def front(self):
        if self.empty():
            raise Exception()
        return self.dq[0]


N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

q = Queue()

for i in range(N):
    c = command[i]
    if c == 'push':
        q.push(A[i])
    elif c == 'pop':
        print(q.pop())
    elif c == 'size':
        print(q.size())
    elif c == 'empty':
        print(q.empty())
    elif c == 'front':
        print(q.front())