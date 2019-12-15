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


def Entr(img,k):

    
    M=img.shape[0]
    N=img.shape[1]
    
    #정보 엔트로피
    c4=np.zeros(256, dtype=int)
    for i in range(M):
        for j in range(N):
            c4[img[i,j,k]]+=1
    #print(c4)
    c4=c4/(M*N)
    #print(c4)

    c5=log2(c4)
    #print(c5)

    Ent=(-1)*dotprod(c4,c5)
    print("Entropy =", end=" ")
    print(Ent)
    
    return


#################################################
if __name__ == '__main__':



   
    file = 'cube_encrypt.png'
    img = cv2.imread(file, 1)
    Entr(img,0)
    Entr(img,1)
    Entr(img,2)

#################################################
    
