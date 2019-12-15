import numpy as np
import cv2
from copy import copy
import operator as op
import random as rd
from matplotlib import pyplot as plt


def log2(c):
    d=np.zeros(len(c))
    for i in range(len(c)):
        p=c[i]
        if p>0:
            d[i]=np.log2(p)

    return d


def dotprod(a,b):
    if len(a)!=len(b):
        print("Length ERROR")
        return
    d=0
    for i in range(len(a)):
        d+=a[i]*b[i]

    return d


#################################################
if __name__ == '__main__':
    file = 'cube_encrypt.png'
    img = cv2.imread(file, 1)

    
    cv2.imshow('image', img)


    M=img.shape[0]
    N=img.shape[1]


    a=2000
    
    num=[]
    for i in range(254):
        for j in range(254):
            txt=i,j
            num.append(txt)
    
    rd.shuffle(num)
    num=num[0:a]
    len(num)
    print(num[255][1])




    color=0
    print(color)
    
    #가로쌍 산포도, 상관계수
    c1=np.zeros([2,a])
    for i in range(a):
        c1[0,i]=img[num[i][0],num[i][1],color]
        c1[1,i]=img[num[i][0]+1,num[i][1],color]

    plt.subplot(3,3,1), plt.plot(c1[0],c1[1],"ro",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Horizontal")
    print("Horizontal =", end=" ")
    print(np.corrcoef(c1[0],c1[1])[1,0])


    #세로쌍 산포도, 상관계수
    c2=np.zeros([2,a])
    for i in range(a):
        c2[0,i]=img[num[i][0],num[i][1],color]
        c2[1,i]=img[num[i][0],num[i][1]+1,color]
    
    plt.subplot(3,3,4), plt.plot(c2[0],c2[1],"ro",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Vertical")
    print("Vertical =", end=" ")
    print(np.corrcoef(c2[0],c2[1])[1,0])

    #대각쌍 산포도, 상관계수
    c3=np.zeros([2,a])
    for i in range(a):
        c3[0,i]=img[num[i][0],num[i][1],color]
        c3[1,i]=img[num[i][0]+1,num[i][1]+1,color]
        
    plt.subplot(3,3,7), plt.plot(c3[0],c3[1],"ro",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Diagonal")
    print("Diagonal =", end=" ")
    print(np.corrcoef(c3[0],c3[1])[1,0])



    color=1
    print(color)

    #가로쌍 산포도, 상관계수
    c1=np.zeros([2,a])
    for i in range(a):
        c1[0,i]=img[num[i][0],num[i][1],color]
        c1[1,i]=img[num[i][0]+1,num[i][1],color]

    plt.subplot(3,3,2), plt.plot(c1[0],c1[1],"go",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Horizontal")
    print("Horizontal =", end=" ")
    print(np.corrcoef(c1[0],c1[1])[1,0])


    #세로쌍 산포도, 상관계수
    c2=np.zeros([2,a])
    for i in range(a):
        c2[0,i]=img[num[i][0],num[i][1],color]
        c2[1,i]=img[num[i][0],num[i][1]+1,color]
        
    plt.subplot(3,3,5), plt.plot(c2[0],c2[1],"go",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Vertical")
    print("Vertical =", end=" ")
    print(np.corrcoef(c2[0],c2[1])[1,0])

    #대각쌍 산포도, 상관계수
    c3=np.zeros([2,a])
    for i in range(a):
        c3[0,i]=img[num[i][0],num[i][1],color]
        c3[1,i]=img[num[i][0]+1,num[i][1]+1,color]
        
    plt.subplot(3,3,8), plt.plot(c3[0],c3[1],"go",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Diagonal")
    print("Diagonal =", end=" ")
    print(np.corrcoef(c3[0],c3[1])[1,0])


    color=2
    print(color)
    
    #가로쌍 산포도, 상관계수
    c1=np.zeros([2,a])
    for i in range(a):
        c1[0,i]=img[num[i][0],num[i][1],color]
        c1[1,i]=img[num[i][0]+1,num[i][1],color]

    plt.subplot(3,3,3), plt.plot(c1[0],c1[1],"bo",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Horizontal")
    print("Horizontal =", end=" ")
    print(np.corrcoef(c1[0],c1[1])[1,0])


    #세로쌍 산포도, 상관계수
    c2=np.zeros([2,a])
    for i in range(a):
        c2[0,i]=img[num[i][0],num[i][1],color]
        c2[1,i]=img[num[i][0],num[i][1]+1,color]    
    plt.subplot(3,3,6), plt.plot(c2[0],c2[1],"bo",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Vertical")
    print("Vertical =", end=" ")
    print(np.corrcoef(c2[0],c2[1])[1,0])

    #대각쌍 산포도, 상관계수
    c3=np.zeros([2,a])
    for i in range(a):
        c3[0,i]=img[num[i][0],num[i][1],color]
        c3[1,i]=img[num[i][0]+1,num[i][1]+1,color]
        
    plt.subplot(3,3,9), plt.plot(c3[0],c3[1],"bo",ms=0.3)
    plt.axis([0, 255, 0, 255])
    plt.xlabel("Diagonal")
    print("Diagonal =", end=" ")
    print(np.corrcoef(c3[0],c3[1])[1,0])



    #그래프 공간크기 제어
    plt.subplots_adjust(hspace=0.35, wspace=0.35)    



    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#################################################
    
