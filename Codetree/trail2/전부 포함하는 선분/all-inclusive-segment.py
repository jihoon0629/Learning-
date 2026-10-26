n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments2 = segments[:]
first_line = min(segments, key = lambda x: x[0])
last_line = max(segments, key = lambda x: x[1])
segments.remove(first_line)
segments2.remove(last_line)
print(min((max(segments, key = lambda x: x[1])[1] - min(segments, key = lambda x: x[0])[0], max(segments2, key = lambda x: x[1])[1] - min(segments2, key = lambda x: x[0])[0])))