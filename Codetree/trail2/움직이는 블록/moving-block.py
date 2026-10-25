n = int(input())
blocks = [int(input()) for _ in range(n)]
point = 0
av = sum(blocks) // n
for i in range(n):
    if blocks[i] > av:
        point += blocks[i] - av
print(point)