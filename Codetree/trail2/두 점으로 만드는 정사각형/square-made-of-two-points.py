x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())
x_arr = [x1,x2,a1,a2]
y_arr = [y1,y2,b1,b2]
print(max((max(x_arr) - min(x_arr)), (max(y_arr) - min(y_arr))) ** 2)