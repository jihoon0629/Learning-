n = int(input())

class weather:
    def __init__(self, date, day, sky):
        self.date = date
        self.day = day
        self.sky = sky

arr = [tuple(input().split()) for i in range(n)]
days = [weather(date, day, sky) for date, day, sky in arr]


find = False

for i, elem in enumerate(days):
    if elem.sky == 'Rain' and find == False:
        fast_rain = i
        find = True
    if elem.sky == 'Rain' and elem.date < days[fast_rain].date:
        fast_rain = i
    
that_day = days[fast_rain]

print(f"{that_day.date} {that_day.day} {that_day.sky}")