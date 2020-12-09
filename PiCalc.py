from math import floor


class PiCalc:
    # Num == number of decimals of approx
    def __init__(self, num):
        self.num = num

    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num

    def boundCap(self):
        if self.num > 10:
            return "Please try a number below 10!"
        else:
            return ""

    def calculation(self):
        if self.boundCap() == "":
            e = 10 ** (-1 * self.num)
            n = (10 ** self.num - 1) / 2
            if not isinstance(n, int):
                n = floor(n + 1)
            return self.summation(n)
        else:
            return ""

    def summation(self, n):
        i = 0
        total = 0
        while i < n:
            if i % 2 == 1:
                total = total - (float(1)/(2*i + 1))
            else:
                total = total + (float(1)/(2*i + 1))
            i += 1
        return 4 * total

obj = PiCalc(4)
print(obj.boundCap())
print(obj.calculation())

