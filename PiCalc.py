from math import floor
import math

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
    def calculation_slow_approx(self):
        if self.boundCap() == "":
            n = getNumberTermsSlowApprox()
            return self.summation(n)
        else:
            return ""
    
    def getNumberTermsSlowApprox(self):
        e = 10 ** (-1 * (self.num + 1)) #using 10^(-n) doesn't guarantee nth decimal place is correct. Using 10^(-(n+1)) as thereshold does
        n = float((e ** (-1) - 1))/2
        if not isinstance(n, int):
            n = floor(n + 1)
        return n
    
    def getNumberTermsMachinApprox(self):
        errorBound = math.log(10 ** (-1*(self.num + 1)), float(1/25)) #error bound is (1/25)^n according to https://www.math.brown.edu/reschwar/M10/machin.pdf 
        if not isinstance(errorBound, int):
            n = floor(errorBound + 1)
        return n

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
    
    """
    faster approximation for pi but with less terms required. Machin formula

    Identity: pi = 16arctan(1/5) - 4arctan(1/239) according to 
    """
    def fast_pi_approximation(self):
        if (self.boundCap() == ""):
            n = self.getNumberTermsMachinApprox()
            return self.machinFormula(n)
        else:
            return -1
    
    def machinFormula(self, n):
        i = 0
        total = 0
        term = 0
        while i < n:
            term = self.termMagnitude(i)
            if i % 2 == 1:
                total = total - term
            else:
                total = total + term
            i += 1
        return total
    
    def termMagnitude(self, i):
        return float((16 * (0.2 ** (2*i + 1)) - 4 * ((1/239) ** (2*i + 1)))/(2*i + 1))


obj = PiCalc(1)
print("FASTER MACHIN APPROXIMATION\n")
for i in range(1, 11):
    obj.setNum(i)
    print("pi to {} decimal place with {} terms summed".format(i, obj.getNumberTermsMachinApprox()))
    print("approximation to pi is {} to {} decimal places of accuracy".format(obj.fast_pi_approximation(), i))

# print("SLOW APPROXIMATION\n")
# for i in range(1, 11):
#     obj.setNum(i)
#     print("pi to {} decimal place with {} terms summed".format(i, obj.getNumberTermsSlowApprox()))
    

