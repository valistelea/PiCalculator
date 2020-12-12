
import math
import matplotlib.pyplot as plt
import numpy as np

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
        elif self.num == 0:
            return "Please try a number greater than 0 but less than 10!"
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
            n = math.floor(n + 1)
        return n
    
    def getNumberTermsMachinApprox(self):
        errorBound = math.log(10 ** (-1*(self.num + 1)), float(1/25)) #error bound is (1/25)^n according to https://www.math.brown.edu/reschwar/M10/machin.pdf 
        if not isinstance(errorBound, int):
            n = math.floor(errorBound + 1)
        return n

    def summation(self, n):
        i = 0
        total = 0
        while i < n:
            if i % 2 == 1:
                total = total - (float(1)/(2*i+1))
            else:
                total = total + (float(1)/(2*i+1))
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
    
    def plotSlowApproximation(self):
        fig, ax = plt.subplots()
        x = [1,2,3,4,5,6,7,8,9,10]
        dummy_pi_calc = PiCalc(1)
        y = []
        for elem in x:
            dummy_pi_calc.setNum(elem)
            y.append(dummy_pi_calc.getNumberTermsSlowApprox())
        xModel = [1,2,3,4,5,6,7,8,9,10]
        yModel = [5*(10 ** elem) for elem in xModel]
        ax.plot(xModel, yModel, color="red", label='y=5*(10)^x')
        plt.legend(fontsize=9) 
        plt.scatter(x,y)
        ax.set_xlabel("Decimal places")
        ax.set_ylabel("Number of terms needed")
        ax.set_title("Slow approximation of pi performance")
        ax.xaxis.set_label_coords(1.05,0)
        plt.show()

    def plotFastApproximation(self):
        fig, ax = plt.subplots()
        x_fast = [1,2,3,4,5,6,7,8,9,10]
        dummy_pi_calc = PiCalc(1)
        y_fast = []
        for elem in x_fast:
            dummy_pi_calc.setNum(elem)
            y_fast.append(dummy_pi_calc.getNumberTermsMachinApprox())
        ax.scatter(x = x_fast, y = y_fast)
        m, b = np.polyfit(x_fast, y_fast, 1)
        y_model = [m*elem + b for elem in x_fast]
        ax.plot(x_fast, y_model, color="red", label='y={:.2f}x+{:.2f}'.format(m,b))
        plt.legend(fontsize=9)  
        ax.set_xlabel("Decimal Places")
        ax.set_ylabel("Number of terms needed")
        ax.set_title("Machin approximation of pi performance")
        ax.xaxis.set_label_coords(1.05,0)
        plt.show()
    def termMagnitude(self, i):
        return float((16 * (0.2 ** (2*i + 1)) - 4 * ((1/239) ** (2*i + 1)))/(2*i + 1))


def main():
    obj = PiCalc(1)
    # print("FASTER MACHIN APPROXIMATION\n")
    # for i in range(1, 11):
    #     obj.setNum(i)
    #     print("pi to {} decimal place with {} terms summed".format(i, obj.getNumberTermsMachinApprox()))
    #     print("approximation to pi is {} to {} decimal places of accuracy".format(obj.fast_pi_approximation(), i))

    # print("SLOW APPROXIMATION\n")
    # for i in range(1, 11):
    #     obj.setNum(i)
    #     print("pi to {} decimal place with {} terms summed".format(i, obj.getNumberTermsSlowApprox()))
        

    obj.plotSlowApproximation()
    obj.plotFastApproximation()

if __name__ == '__main__':
    main()

