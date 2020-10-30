

import math

def func(x):
    return 1/(1+x*x)

def divde(a,b,n):
    h = abs(a-b)/n
    X = []
    Y = []
    for i in range(0,n+1):
        X.append(a + h*i)
        Y.append(func(X[i]))
    return X,Y


def Fenduan(a,b,n,x):
    h = abs(a-b)/n
    num = math.floor(abs(x - a)/h)
    X,Y = divde(a,b,n)
    res = Y[num]*(x - X[num +1])/(X[num] - X[num +1]) + Y[num+1]*(x - X[num])/(X[num+1] - X[num])
    return  res


def Lagrange(a,b,x,n):
    t = 0
    y = 0
    k = 0
    X,Y = divde(a,b,n)
    for k in range(0,n+1):
        t = 1
        for j in range(0,n+1):
            if j != k :
                t *= (x- X[j])/(X[k] - X[j])
        y += t*Y[k]
    return y


def calErr(cal,x):
    return func(x) - cal

def formatChange(x):
    return format(x,'.6f')

import matplotlib.pyplot as plt
import numpy as np

def showRunger(a,b,n,Arr):
    X,Y = divde(a,b,n)
    Ry = []
    rx = np.arange(-5, 5, 0.01)
    y = func(rx)
    plt.plot(rx, y, linewidth=3,c = 'y',label='y = 1/(1+x^2)')
    plt.legend()
    for i in Arr:
        Ry = Lagrange(a, b, rx, i)
        plt.plot(rx, Ry, label='Runger n= ' + str(i))
        plt.legend()
    plt.show()
    # for i in range(0,101):
    #     x =  a + i*abs(a-b)/101
    #     Ry.append(Lagrange(a,b,x,n))

def showDifferRunger(a,b,Arr):
    for i in Arr:
        showRunger(a,b,i)

def main():
    print("X".ljust(10) + "y(精确)".ljust(10) +"y(拉格朗日)".ljust(10)+"y(分段线性)".ljust(10)+"误差(拉格朗日)".ljust(10)+"误差(分段线性)".ljust(10))
    l05 = Lagrange(-5,5,0.5,10)
    f05 = Fenduan(-5,5,10,0.5)
    print(formatChange(0.5).ljust(10) + formatChange(func(0.5)).ljust(12)+ formatChange(l05).ljust(14) + formatChange(f05).ljust(12) + formatChange(calErr(l05,0.5)).ljust(15) + formatChange(calErr(f05,0.5)).ljust(12)  )
    l45 = Lagrange(-5, 5, 4.5, 10)
    f45 = Fenduan(-5, 5, 10, 4.5)
    print(formatChange(4.5).ljust(10) + formatChange(func(4.5)).ljust(12)+ formatChange(l45).ljust(14) + formatChange(f45).ljust(12) + formatChange(calErr(l45,4.5)).ljust(15) + formatChange(calErr(f45,4.5)).ljust(12)  )
    Arr = [3,5,7,10,15]
    # showDifferRunger(-5,5,Arr)
    showRunger(-5,5,10,Arr)

if __name__ == '__main__':
    main()