from collections import deque

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

dq = deque()

for i in range(n):
    c = cmd[i]
    if c == 'push_front':
        dq.appendleft(num[i])
    elif c == 'push_back':
        dq.append(num[i])
    elif c == 'pop_front':
        print(dq.popleft())
    elif c == 'pop_back':
        print(dq.pop())
    elif c == 'size':
        print(len(dq))
    elif c == 'empty':
        print(int(not dq))
    elif c == 'front':
        print(dq[0])
    elif c == 'back':
        print(dq[-1])

