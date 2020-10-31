

def func(x):
    return x**3-x-1

def dfunc(x):
    return 3*pow(x,2)-1

def new(x0,err,n,m,ep=1e-6):
    k = 0
    myk = []
    myk.append(k)
    x = []
    myl = []
    myi = []
    while k<n:
        if(dfunc(x0) == 0):
            return
        i = 0 #目前已经下山0次
        lambda_ = 1# 下山因子取1
        myi.append(i)
        myl.append(lambda_)
        flag = 1
        while flag ==1:
            x1 = x0 - lambda_*(func(x0)/dfunc(x0))
            x.append(x1)
            if ((abs(func(x1)) - abs(func(x0)))<0):
                # break
                flag = 0
            else:
                i += 1 # 继续下山
                if lambda_ >= 0.00001:
                    lambda_ *= 0.5
                    lambda_ = float(format(lambda_,'.6f'))
                else:
                    lambda_ = 0.00001
                myi.append(i)
                myl.append(lambda_)
                if(i >= m): # 下山超过规定次数
                    print("please enter anthor x0")
                    return x, myk, myi, myl
        if abs(x1 - x0)<err :
            # print(myk)
            # print(x)
            # print(myi)
            # print(myl)
            return x,myk,myi,myl
        k += 1 #再次迭代
        x0 = x1
        myk.append(k)
    return "failed"

def changeFormat(list):
    for i in range(0,len(list)):
        list[i] = format(list[i],'.6f').ljust(9)
    return list

def main():
    x0 = 0.1
    print("x0 = " + str(x0))
    print("迭代次数".ljust(9) + "下山次数".ljust(9) + "λ".ljust(19) + "迭代值".ljust(9))


    x,k,i,l = new(x0,0.000001,10,25)
    # print(x)
    # print(len(x))
    # print(len(k))
    # print(k)
    # print(len(i))
    # print(i)
    # print(len(l))
    # print(l)
    x = changeFormat(x)
    # print(x)
    k1 = -1
    for i1 in range(0,len(x)) :
        if(i[i1] == 0):
            k1 += 1
        print(str(k[k1]+1).ljust(12) + str(i[i1]+1).ljust(12) + str(l[i1]).ljust(19) + str(x[i1]))


if __name__ == '__main__':
    main()