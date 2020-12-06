import math
class Polynomial:
    def __init__(self, coefficients):
        self._coef = coefficients

    def __str__(self):
        power=0
        output=''
        for x in range(len(self._coef)):
            output+=str(self._coef[-x-1])+'x^'+str(power)+' '
            power+=1
        return output

    def eval(self, x):
        calculation = 0.0
        power = len(self._coef)
        for y in range(power):
            print(math.pow(x,power)*self._coef[y])
            calculation+= math.pow(x,power)*self._coef[y]
            power-=1
        return calculation

    def __add__(self, x):
        if len(self._coef)>=len(x._coef):
            Barr = self._coef
            Sarr = x._coef
        else:
            Barr = x._coef
            Sarr = self._coef
        for x in range(len(Sarr)):
            Barr[-1-x]+=Sarr[-1-x]
        return Barr

    def __iadd__(self, x):
        return self + x

    def __mul__(self, x):
        mularr = []
        temp = []
        print(x)
        for x in range(len(self._coef)):
            for y in range(len(x._coef)):
                #-x-1 -y-1
                temp.append(self._coef[x]*x[y])
            mularr.append(temp)
            temp=[]
        print(mularr)

f= Polynomial([-5, 0, 2, 0, 1])
z= Polynomial([5, 0, 2, 0])
print(f*z)