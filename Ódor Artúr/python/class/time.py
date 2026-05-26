class time:
    def __init__(self, hour, minute, second):
        minute += second // 60
        self.second = second % 60
        hour += minute // 60
        self.minute = minute % 60
        self.hour = hour % 24

    def __repr__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    

    def __add__(self, other):
        pontosido = (self.hour *24*60 + self.minute *60 + self.second) + (other.hour*24*60 + other.minute*60+other.second)
        return time(pontosido)
    

    def __sub__(self, other):


ido = time(10, 20, 30)
ido2 = time(3, 62, 66)
print(ido2)
print(ido2 - ido)
print(ido + ido2)
