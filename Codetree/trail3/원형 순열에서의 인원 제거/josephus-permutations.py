from collections import deque

class queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, a):
        self.dq.append(a)

    def pop(self):
        if self.empty():
            raise Exception()
        return self.dq.popleft()

    def empty(self):
        return int(not self.dq)
    
    def size(self):
        return len(self.dq)
    
    def front(self):
        if self.empty():
            raise Exception()
        return self.dq[0]



n, k = map(int, input().split())
q = queue()
dead = queue()
for i in range(1,n+1):
    q.push(i)
while q.size() > 1:
    for i in range(1,k):
        q.push(q.pop())
    dead.push(q.pop())
dead.push(q.pop())
for i in range(dead.size()):
    print(dead.pop(),end=' ')
