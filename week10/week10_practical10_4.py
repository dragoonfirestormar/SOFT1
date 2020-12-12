import math
class Polynomial:
    def __init__(self, coefficients):
        self._coef = coefficients

    def __str__(self):
        power=0
        output=''
        for x in range(len(self._coef)):
            if not abs(self._coef[-x-1]) == 0:
                output+=('+ ' if self._coef[-x-1]>0 else '- ' )+str(abs(self._coef[-x-1]))+'x^{'+str(power)+'} '
            power+=1
        return output[2:]

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
        a = len(self._coef)
        b = len(x._coef)
        A = self._coef
        B = x._coef
        aP = a-1
        bP = b-1
        temp = [0]*(aP+bP+1)
        for x in range(a):
            for y in range(b):
                temp[-aP-bP-1]=(A[x]*B[y])
                bP-=1
            aP = aP-1
            bP = b-1
            mularr.append(temp)
            temp=[0]* (aP+bP+1)
        X = [0]
        for x in mularr:
            if len(X)>=len(x):
                Barr = X
                Sarr = x
            else:
                Barr = x
                Sarr = X
            for y in range(len(Sarr)):
                Barr[-1-y]+=Sarr[-1-y]
            X = Barr
        return (X)

    def to_latex(self):
        return self

f= Polynomial([3,0,2])
z= Polynomial([4,0,-7,1])
print(z.to_latex())