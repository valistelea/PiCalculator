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

    """
    Link for inspiration: https://math.stackexchange.com/questions/1031363/how-many-terms-does-it-take-in-the-expansion-of-arctanx-to-get-pi-to-10-decima
    """
    def calculation(self):
        if self.boundCap() == "":
            e = 10 ** (-1 * (self.num + 1)) #using 10^(-n) doesn't guarantee nth decimal place is correct. Using 10^(-(n+1)) as thereshold does
            n = float((e ** (-1) - 1))/2
            if not isinstance(n, int):
                n = floor(n + 1)
            #return n
            return self.summation(n)
        else:
            return ""

    def summation(self, n):
        i = 0
        total = 0
        while i < n:
            if i % 2 == 1:
                total = total - (float(1/(2*i + 1)))
            else:
                total = total + (float(1/(2*i + 1)))
            i += 1
        return 4 * total

obj = PiCalc(5)
print(obj.boundCap())
print(obj.calculation())