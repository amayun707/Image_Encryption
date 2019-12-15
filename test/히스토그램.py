import numpy as np
import cv2
from copy import copy
import operator as op
import random as rd
from matplotlib import pyplot as plt




#################################################
if __name__ == '__main__':
    file = 'cube_encrypt.png'
    #file = '1-1.color_Lena.png'
    img = cv2.imread(file, 1)

    
    cv2.imshow('image', img)

    plt.figure(1, figsize=(6, 4))

    M=img.shape[0]
    N=img.shape[1]

    #print(np.zeros(10, dtype=int))
    
    color=0
    s=slice(M*N*(color),M*N*(color+1),1)
    #히스토그램
    #print(img.ravel()[s])
    #print(M*N*(color+1))
    plt.subplot(1,1,1), plt.hist(img.ravel()[s],histtype='step',bins=256,color="red")
    plt.ylim([0,1500])
    plt.axis([0, 255, 0, 1500]) #y축 격자범위

    color=2
    s=slice(M*N*(color),M*N*(color+1),1)
    #히스토그램
    plt.subplot(1,1,1), plt.hist(img.ravel()[s],histtype='step',bins=256,color="blue")
    plt.ylim([0,1500])
    plt.axis([0, 255, 0, 1500]) #y축 격자범위

    color=1
    s=slice(M*N*(color),M*N*(color+1),1)
    #히스토그램
    plt.subplot(1,1,1), plt.hist(img.ravel()[s],histtype='step',bins=256,color="green")
    plt.ylim([0,1500])
    plt.axis([0, 255, 0, 1500]) #y축 격자범위
    


    #그래프 공간크기 제어
    plt.subplots_adjust(wspace=0.35)



    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#################################################
    
