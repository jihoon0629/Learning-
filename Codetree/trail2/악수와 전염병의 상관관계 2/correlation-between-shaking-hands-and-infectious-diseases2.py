N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
class developer:
    def __init__(self, sick=False, spread_count=0):
        self.sick = sick
        self.spread_count = spread_count

    def infection(self):
        if self.sick == False:
            self.sick = True
            self.spread_count = K

    def inf(self, other):
        if (self.sick == True) and (self.spread_count > 0):
            if other.sick == False:
                developer.infection(other)
            else:
                if other.spread_count > 0:
                    other.spread_count -= 1
            self.spread_count -= 1
        else:
            if other.sick == True and other.spread_count > 0:
                developer.infection(self)
                other.spread_count -= 1


arr = [developer() for _ in range(N)]
arr[P-1].infection()
# Please write your code here.
handshakes.sort(key = lambda x: x[0])
for i in range(T):
    developer.inf(arr[handshakes[i][1]-1], arr[handshakes[i][2]-1])
for i in arr:
    print(int(i.sick),end='')