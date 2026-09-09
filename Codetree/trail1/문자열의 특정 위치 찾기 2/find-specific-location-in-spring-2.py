arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']
a = input()
count=0
for i in range(5):
    if arr[i][2] == a or arr[i][3] == a:
        count+=1
        print(arr[i])
print(count)