import numpy as np
import cv2
import operator as op
from copy import copy

def ca(cav,Rul):								#CA 수열 생성 :  5-이웃
    k=len(cav)
    tmp=copy(cav)

    cav[0]=(tmp[0]*Rul[0]+tmp[1]+tmp[2])%2
    cav[1]=(tmp[0]+tmp[1]*Rul[1]+tmp[2]+tmp[3])%2

    cav[k-2]=(tmp[k-1]+tmp[k-2]*Rul[k-2]+tmp[k-3])%2
    cav[k-1]=(tmp[k-1]*Rul[k-1]+tmp[k-2])%2
    for i in range(2,k-2):
        cav[i]=(tmp[i-1]+tmp[i]*Rul[i]+tmp[i+1]+tmp[i+2])%2

    return cav

def crypt(img,cav,Rul1,Rul2):							# 암호화 함수
    nVec=np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype=int)
    for k in range(3):        
        for i in range(img.shape[0]):
            if i==0:
                _cav=cav[k]
            for j in range(img.shape[1]):
                if j==0:
                    if i==0:
                        _cav=ca(_cav,Rul1)
                    else:							# 첫번째줄 구할 때, [i-1,j,k] 자리에 있는 벡터 값을 2진수 변환하고, 쪼개서 길이가 8인 리스트로 만듬
                        c=str(bin(nVec[i-1,j,k]))
                        cc=[]
                        for m in c[2:]:
                            cc.append(int(m))
                        while len(cc) != 8:
                            cc.insert(0,0)
                        _cav=ca(cc,Rul1)              
                else:								# 아래 방향으로 구할 때, [i, j-1, k]자리에 있는 벡터 값을 2진수 변환하고, 쪼개서 길이가 8인 리스트로 만듬
                    c=str(bin(nVec[i,j-1,k]))
                    cc=[]
                    for m in c[2:]:
                        cc.append(int(m))
                    while len(cc) != 8:
                        cc.insert(0,0)                    
                    _cav=ca(cc,Rul2)
                for t in range(8):
                    nVec[i,j,k]+=(_cav[t]*(2**(7-t)))  

    for k in range(3):							# 이미지와 위에서 구한 벡터 값을  XOR 해서 암호화한다.
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img[i,j,k]=op.xor(img[i,j,k],nVec[i,j,k])    
    return np.array(img,copy=True)


#################################################
if __name__ == '__main__':
    file = '1-1.color_Lena.png'
    img = cv2.imread(file, 1)

    Rul1=[0,1,0,1,1,1,0,1]
    Rul2=[0,1,1,1,0,1,0,1]

    cav =[[0,1,1,0,1,1,0,0],[0,0,1,1,1,0,0,1],[1,0,1,0,1,0,1,0]]   #초기치 1
    #cav =[[1,1,1,0,1,1,0,0],[1,0,1,1,1,0,0,1],[0,0,1,0,1,0,1,0]]   # 변경 2
    #암호화
    img2=crypt(img,cav,Rul1,Rul2)
    
    cv2.imwrite('encrypt.png',img2)

#################################################
    
