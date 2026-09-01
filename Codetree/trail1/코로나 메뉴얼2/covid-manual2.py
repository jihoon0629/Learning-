a_cnt=0
b_cnt=0
c_cnt=0
d_cnt=0

for i in range(3):
    arr=input().split()
    if arr[0]=='Y':
        if int(arr[1]) >= 37:
            a_cnt+=1
        else:
            c_cnt+=1
    else:
        if int(arr[1]) >= 37:
            b_cnt+=1
        else:
            d_cnt+=1
    
print(f"{a_cnt} {b_cnt} {c_cnt} {d_cnt}",end=' ')
if a_cnt>=2:
    print('E')