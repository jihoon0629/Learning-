unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class inf:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

information = inf(unlock_code, wire_color, seconds)
print(f"""code : {information.code}
color : {information.color}
second : {information.sec}""")