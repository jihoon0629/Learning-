arr = [list(map(int, input().split())) for _ in range(19)]
vic = False
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            color = arr[i][j]
            if i>=2 and i<=16 and arr[i-1][j] == color and arr[i-2][j] == color and arr[i+1][j] == color and arr[i+2][j] == color:
                print(color)
                print(i+1,j+1)
                vic = True
            if j>=2 and j<=16 and arr[i][j-1] == color and arr[i][j-2] == color and arr[i][j+1] == color and arr[i][j+2] == color:
                print(color)
                print(i+1,j+1)
                vic = True
            if i>=2 and i<=16 and j>=2 and j<=16 and arr[i-1][j-1] == color and arr[i-2][j-2] == color and arr[i+1][j+1] == color and arr[i+2][j+2] == color:
                print(color)
                print(i+1,j+1)
                vic = True
            if i>=2 and i<=16 and j>=2 and j<=16 and arr[i-1][j+1] == color and arr[i-2][j+2] == color and arr[i+1][j-1] == color and arr[i+2][j-2] == color:
                print(color)
                print(i+1,j+1)
                vic = True
if not vic:
    print(0)

