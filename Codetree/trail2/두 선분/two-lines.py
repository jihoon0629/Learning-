x1, x2, x3, x4 = map(int, input().split())
x = [x1,x2]
y = [x3,x4]
inter = False
for elem in x:
    if x3<=elem<=x4:
        inter = True
for elem in y:
    if x1<=elem<=x2:
        inter = True
if inter:
    print("intersecting")
else:
    print("nonintersecting")