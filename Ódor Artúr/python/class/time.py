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
        if self.second + other.second <60:
            msp = self.second + other.second
        elif self.second + other.second >=60:
            self.minute += 1
            msp = self.second + other.second - 60
        if self.minute + other.minute <60:
            p = self.minute + other.minute
        elif self.minute + other.minute >=60:
            self.hour += 1
            p = self.minute + other.minute - 60
        if self.hour + other.hour <24:
            o = self.hour + other.hour
        elif self.hour + other.hour >= 24:
            o = self.hour + other.hour - 24
        return time(o, p, msp)
    

    def __sub__(self, other):
        if self.second - other.second >0:
            msp = self.second - other.second
        elif self.second - other.second <=0:
            self.minute -= 1
            msp = self.second - other.second + 60
        if self.minute - other.minute >0:
            p = self.minute - other.minute
        elif self.minute - other.minute <=0:
            self.hour -= 1
            p = self.minute - other.minute + 60
        if self.hour - other.hour >0:
            o = self.hour - other.hour
        elif self.hour - other.hour <= 0:
            o = self.hour - other.hour + 24
        return time(o, p, msp)


ido = time(10, 20, 30)
ido2 = time(3, 62, 66)
print(ido2)
print(ido2 - ido)
print(ido + ido2)
