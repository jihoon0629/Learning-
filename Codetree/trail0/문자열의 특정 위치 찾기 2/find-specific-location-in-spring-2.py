cnt = 0
l = ["apple","banana","grape","blueberry","orange"]
a = input()

for i in range(5):
    if l[i][2] == a or l[i][3] == a:
        print(l[i])
        cnt+=1
print(cnt)