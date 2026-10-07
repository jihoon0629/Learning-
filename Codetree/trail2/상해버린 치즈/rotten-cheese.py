human, cheese_cnt, eat_record_cnt, sick_record_cnt = map(int,input().split())
eat_record = [list(map(int,input().split())) for _ in range(eat_record_cnt)]
sick_record = [list(map(int,input().split())) for _ in range(sick_record_cnt)]
eat_record.sort(key = lambda x: (x[0],x[1],x[2]))
delete = []
max_cnt = 0
arr = [i for i in range(1,cheese_cnt+1)]
for i in range(len(eat_record)):
    for j in range(i+1,len(eat_record)):
        if eat_record[i][0] == eat_record[j][0] and eat_record[i][1] == eat_record[j][1]:
            delete.append(j)
for i in range(len(eat_record)-1,-1,-1):
    if i in delete:
        eat_record.pop(i)
for i in range(len(sick_record)):
    for j in range(len(eat_record)):
        if sick_record[i][0] == eat_record[j][0] and sick_record[i][1] <= eat_record[j][2]:
            if eat_record[j][1] in arr:
                arr.pop(arr.index(eat_record[j][1]))               
for i in range(len(sick_record)):
    sick_person = sick_record[i][0]
    sick_time = sick_record[i][1]
    ate_before_sick = []
    for j in range(len(eat_record)):
        if eat_record[j][0] == sick_person and eat_record[j][2] < sick_time:
            ate_before_sick.append(eat_record[j][1])
    new_arr = []
    for cheese in arr:
        if cheese in ate_before_sick:
            new_arr.append(cheese)
    arr = new_arr
for i in arr:
    cnt = 0
    for j in range(len(eat_record)):
        if eat_record[j][1] == i:
            cnt+=1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)