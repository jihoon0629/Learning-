n, m, p = map(int, input().split())
human = [chr(ord('A') + i) for i in range(n)]
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]
arr = []
if u[p-1] == 0:
    print()
else:
    for i in range(u.index(u[p-1]),m):
        if c[i] not in human:
            continue
        else:
            human.pop(human.index(c[i]))
    for i in human:
        print(i,end=' ')