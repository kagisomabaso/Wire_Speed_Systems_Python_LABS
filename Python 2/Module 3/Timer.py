def format(val):
    if val < 10:
        val = "0" + str(val)
    else:
        val = str(val)
    return val

class Timer:
    def __init__(self,hr=0,mm=0,sc=0):
        self.__hr = hr
        self.__mm = mm
        self.__sc = sc
        self.__str__()

    def __str__(self):
        return format(self.__hr) + ":" + format(self.__mm) + ":" + format(self.__sc)

    def next_second(self):
        self.__sc += 1
        if self.__sc > 59 :
            self.__sc = 0

            self.__mm += 1
            if self.__mm > 59 :
                self.__mm = 0

                self.__hr += 1
                if self.__hr > 23:
                    self.__hr = 0

    def prev_second(self):
        self.__sc -= 1
        if self.__sc < 0:
            self.__sc = 59

            self.__mm -= 1
            if self.__mm < 0:
                self.__mm = 59

                self.__hr -= 1
                if self.__hr < 0:
                    self.__hr = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

