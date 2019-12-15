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


def doet(img1,img2,color):
    
    img3=np.zeros((img1.shape[0],img1.shape[1]),dtype=np.uint8)
    
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if img1[i,j,color]>img2[i,j,color]:
                img3[i,j]=img1[i,j,color]-img2[i,j,color]
            else:
                img3[i,j]=img2[i,j,color]-img1[i,j,color]

    return img3



#################################################
if __name__ == '__main__':
    file1 = 'cube_encrypt.png'
    file2 = 'cube_encrypt2.png'
    img1 = cv2.imread(file1, 1)
    img2 = cv2.imread(file2, 1)

    

    M=img1.shape[0]
    N=img1.shape[1]
    color=0


    #NPCR

    c1=0
    for i in range(M):
        for j in range(N):
            if img1[i,j,color]!=img2[i,j,color]:
                c1+=1

    c1=(c1/(M*N))*100

    print("NPCR =", end=" ")
    print(c1)

    np.seterr(over='ignore')
  
    #UACI

    img3=doet(img1,img2,color)
    c2=0
    for i in range(M):
        for j in range(N):
            c2=c2+img3[i,j]

    c2=(c2/(M*N*255))*100
 
    print("UACI =", end=" ")
    print(c2)







    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#################################################
    
