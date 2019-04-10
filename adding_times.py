class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, time_a):
        time_b = Time()
        if (self.second + time_a.second) >= 60:
            self.minute += 1
            time_b.second = (self.second + time_a.second) - 60
        else:
            time_b.second = self.second + time_a.second
        if (self.minute + time_a.minute) >= 60:
            self.hour += 1
            time_b.minute = (self.minute + time_a.minute) - 60
        else:
            time_b.minute = self.minute + time_a.minute
        if (self.hour + time_a.hour) > 24:
            time_b.hour = (self.hour + time_a.hour) - 24
        else:
            time_b.hour = self.hour + time_a.hour
        return time_b

def main():
    time1 = Time(5, 45, 26)
    print(time1)
    time2 = Time(23, 12, 43)
    print(time2)
    print(time1 + time2)
main()
