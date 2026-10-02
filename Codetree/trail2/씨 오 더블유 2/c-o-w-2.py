n = int(input())
S = input()
cnt = 0
for i in range(len(S)):
    for j in range(i,len(S)):
        for k in range(j,len(S)):
            if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                cnt+= 1
print(cnt)