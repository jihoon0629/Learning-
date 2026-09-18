n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A = sorted(A)
B = sorted(B)
same = True
for i in range(n):
    if A[i] != B[i]:
        same = False

if same:
    print('Yes')
else:
    print('No')