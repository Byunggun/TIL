# 핵심: a 사용자 함수 안 b사용자 함수 사용하는 방법 : y=AND(xs[0],xs[1])

#cf. DL9-1 XOR
#and 게이트-tensorflow 사용x numpy사용.
import numpy as np
def AND(x1,x2): #00 01 10 11 => 0 0 0 1
    x=np.array([x1,x2]) #입력 데이터 2개
    w=np.array([0.5,0.5]) #w 2개
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
#명시적 프로그램 작성하면 아래(but 무수히 많은 경우 적용 한계. 따라서 위 처럼 적용)
# def AND(x1, x2):
    # if x1==1 and x2 ==1:
    #     return 1
    # else:
    #     return


#nand 게이트
def NAND(x1, x2):  # 00 01 10 11 => 1 1 1 0
    x = np.array([x1, x2])  # 입력 데이터 2개
    w = np.array([-0.5, -0.5])  # w 2개
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

    # return # 0 or 1

#or 게이트
def OR(x1, x2):  # 00 01 10 11 => 0 1 1 1
    x = np.array([x1, x2])  # 입력 데이터 2개
    w = np.array([0.5, 0.5])  # w 2개
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#xor 게이트
def XOR(x1, x2):  # 00 01 10 11 => 0 1 1 0
    s1=NAND(x1, x2)
    s2=OR(x1,x2)
    yhat=AND(s1,s2)
    return yhat


if __name__ == '__main__':
    print("and게이트:")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y=AND(xs[0],xs[1]) #and 게이트
        print(str(xs)+"->"+str(y))

    print("nand게이트:")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y=NAND(xs[0],xs[1]) #nand 게이트
        print(str(xs)+"->"+str(y))

    print("or게이트:")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y=OR(xs[0],xs[1]) #or 게이트
        print(str(xs)+"->"+str(y))

    print("xor게이트:")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y=XOR(xs[0],xs[1]) #xor 게이트
        print(str(xs)+"->"+str(y))
