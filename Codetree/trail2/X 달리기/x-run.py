X = int(input())
vel = 1
time = 1
dis = X-vel
while True:
    if dis == 0:
        print(time)
        break
    if dis >= sum(i for i in range(1,vel+1)) + vel + 1:
        vel += 1
        time += 1
        dis -= vel
    elif dis >= sum(i for i in range(1,vel+1)):
        time += 1
        dis -= vel
    else:
            time += 1
            vel -= 1
            dis-= vel