arr=[list(map(int,input().split())) for _ in range(3)]
a=input()
arr2=[list(map(int,input().split())) for _ in range(3)]

arr3=[[arr[j][i] * arr2[j][i] for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        print(arr3[i][j],end=' ')
    print()