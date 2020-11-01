
'''
输入：积分区间，误差限
输出：序列Tn，Sn,Cn,Rn 及积分结果
'''

import math
def func(x):
    return math.sin(x)/x


def getT(a,b,err):
    Tn = []
    h = abs(a-b)
    T1 = h*(1 - func(b))/2
    T2 = 111
    flag = 1
    while abs(T2 - T1)>=err :
        if (flag != 1 ):
            h /= 2
            T1 = T2
        flag = 0
        s = 0
        x = a + h/2
        while x<b:
            s += func(x)
            x += h
        T2 = T1/2 + h*s/2
    return T2


def Romberg(a,b,err): # n Rnum
    Tn = []
    Sn = []
    Cn = []
    Rn = []
    r2= 1
    r1 = 0
    h = abs(a - b)
    t1 = h * (1 + func(b))/2
    Tn.append(t1)
    flagk1 = 0
    flagk2 = 0
    flagk3 = 0
    s1 = 0
    c1 = 0
    k = 1
    myk = []
    myk.append(0)
    while (k<4 and abs(r2-r1)>= err):
        if(flagk1 == 1):
            k+=1
            h /= 2
            t1 = t2
            s1 = s2
        if(flagk2 == 1):
            k += 1
            h /= 2
            t1 = t2
            s1 = s2
            c1 = c2
        if (flagk3 == 1):
            k += 1
            h /= 2
            t1 = t2
            s1 = s2
            c1 = c2
            r1 =r2
        s = 0
        x = a + h/2
        while x<b:
            s += func(x)
            x += h
        t2 = t1/2+h*s/2

        s2 = t2 + (t2 - t1)/3
        if (k == 1):
            flagk1 = 1
            flagk2 = 0
            flagk3 = 0
            Tn.append(t2)
            Sn.append(s2)
            myk.append(k)
        c2 = s2 + (s2 - s1)/15
        if(k == 2):
            flagk2 = 1
            flagk1 = 0
            flagk3 = 0
            Tn.append(t2)
            Sn.append(s2)
            Cn.append(c2)
            myk.append(k)
        r2 = c2 + (c2 - c1)/63
        if(k >= 3):
            flagk3 = 1
            flagk2 = 0
            flagk1 = 0
            Tn.append(t2)
            Sn.append(s2)
            Cn.append(c2)
            Rn.append(r2)
            myk.append(k)
    return Tn,Sn,Cn,Rn,myk





def main():
    print ("k".ljust(5)+"Tn".ljust(12)+"Sn".ljust(12)+"Cn".ljust(12)+"Rn".ljust(12))
    t,s,c,r,k = Romberg(0,1,0.00001)
    for i in range(0,len(k)):
        if i == 0:
            print(str(k[i]).ljust(5) + format(t[i],'.7f').ljust(12))
        elif i == 1 :
            print(str(k[i]).ljust(5) +format(t[i],'.7f').ljust(12) + format(s[i-1],'.7f').ljust(12))
        elif i == 2 :
            print(str(k[i]).ljust(5) +format(t[i],'.7f').ljust(12) + format(s[i-2],'.7f').ljust(12)+ format(c[i-2],'.7f').ljust(12))
        elif i >=3 :
            print(str(k[i]).ljust(5) +format(t[i],'.7f').ljust(12) + format(s[i-3],'.7f').ljust(12)+ format(c[i-3],'.7f').ljust(12)+ format(r[i-3],'.7f').ljust(12))

if __name__ == '__main__':
    main()