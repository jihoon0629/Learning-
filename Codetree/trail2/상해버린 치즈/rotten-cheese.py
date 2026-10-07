N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

new_arr = [i for i in range(1, M + 1)]

for i in range(S):
    av_arr = []
    sick_man = sick_p[i]
    sick_time = sick_t[i]
    for j in range(D):
        if p[j] == sick_man and t[j] < sick_time:
            av_arr.append(m[j])
    av_arr = set(av_arr)
    
    for i in range(len(new_arr)-1,-1,-1):
        if new_arr[i] not in av_arr:
            new_arr.pop(i)


max_count = 0
for i in new_arr:
    count = set()
    for j in range(D):
        if m[j] == i:
            count.add(p[j])
    max_count = max(max_count, len(count))
print(max_count)