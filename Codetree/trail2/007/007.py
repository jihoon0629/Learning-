secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class agent:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

spy = agent(secret_code, meeting_point, time)
print(f"""secret code : {spy.secret_code}
meeting point : {spy.meeting_point}
time : {spy.time}""")