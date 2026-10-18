a, b, x, y = map(int, input().split())
arr = [abs(b-a), abs(x-a)+abs(y-b), abs(y-a)+abs(x-b)]
print(min(arr))