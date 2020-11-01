import math

def func(x,y):
    return y - 2*x/y

def preFunc(x):
    return pow(1+2*x,0.5)

def Romberg4(x,y,h,a,b):
    N = math.floor((abs(a-b)/h))
    n = 1
    flag = 0
    Y = []
    for i in range(1,N+1):
        if flag != 0:
            n += 1
            x = x1
            y = y1
        x1 = x + h
        k1 = func(x,y)
        k2 = func(x+h/2,y + h*k1/2)
        k3 = func(x+h/2,y + h*k2/2)
        k4 = func(x1,y + h*k3)
        y1 = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
        Y.append(y1)
        flag = 1
    return Y

def Euler(h,a,b):
    y0 = 1
    N = math.floor((abs(a - b) / h))
    Y = []
    for i in range(1,N+1):
        if i == 1:
            Y.append(y0 + h*y0)
            # print(Y[0])
        else:
            Y.append(Y[i-2] + h*func(a+h*(i-1),Y[i-2]))
    return Y

def AdvancedEuler(x,y,h,a,b):
    N = math.floor((abs(a-b)/h))
    n = 1
    flag = 0
    Y = []
    for i in range(1,N+1):
        if flag != 0:
            n += 1
            x = x1
            y = y1
        x1 = x + h
        yp = y + h*func(x,y)
        yc = y + h*func(x1,yp)
        y1 = (yp + yc)/2
        flag = 1
        Y.append(y1)
    return Y

def changeFormat(list):
    for i in range(0,len(list)):
        list[i] = format(list[i],'.6f').ljust(12)
    return list

def main():
    print("x".ljust(12)+"y(4阶龙格)".ljust(12)+"y(改进)".ljust(12)+"y(欧拉)".ljust(12)+"y(精确)".ljust(12))
    x = []
    prey = []
    for i in range(1,11):
        x.append(format(i/10,'.6f').ljust(12))
        prey.append(format(preFunc(i/10),'.6f').ljust(12))
    y4 = changeFormat(Romberg4(0,1,0.1,0,1))
    yae = changeFormat(AdvancedEuler(0,1,0.1,0,1))
    ye = changeFormat(Euler(0.1,0,1))


    for i in range(1,11):
        print(str(x[i-1]) + str(y4[i-1]) + str(yae[i-1]) + str(ye[i-1]) + str(prey[i-1]))
if __name__ == '__main__':
    main()