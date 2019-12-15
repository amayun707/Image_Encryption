import numpy as np
import cv2

def init(img,cube): # 초기화 함수
    total=img.shape[0]*img.shape[1]*img.shape[2] # 이미지의 크기^3 
    result=total
    while result>7:                 # result가 7이하가 될떄까지
        tmp=int(result**(1.0/3.0))  # 정수형 result^(1/3)
        cube.append(tmp)            # cube 리스트에 추가
        result-=tmp**3              
    cube.append(result)             # 마지막 남은 result 추가

    for i in range(len(cube)-1):
        cube[i]=np.zeros([cube[i],cube[i],cube[i]],dtype=int)
        # cube 리스트에 각각 크기에 맞는 N^3 배열 저장

    cube[-1]=np.zeros([cube[-1],3],dtype=int) # 마지막 나머지 배열 생성

    return cube

def MakeCube(img,cube): # 만든 큐브에 이미지 데이터를 넣는 함수
    idx=0 # 큐브 리스트 인덱스
    x,y,z=0,0,0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):           
                if z==cube[idx].shape[2]: # (x,y,z) 에서 z가 큐브의 크기와 같아질 때
                    z=0
                    y+=1
                if y==cube[idx].shape[1]: # (x,y,z) 에서 y가 큐브의 크기와 같아질 때
                    y=0
                    x+=1
                if x==cube[idx].shape[0]: # (x,y,z) 에서 x가 큐브의 크기와 같아질 때
                    idx+=1                # 다음 큐브 인덱스로 이동
                    x,y,z=0,0,0           # x,y,z 초기화
                    if idx==len(cube)-1:  # 인덱스가 큐브 리스트의 마지막 값을 가리킬 때
                        for i in range(cube[-1].shape[0]):
                            cube[-1][-1-i]=img[img.shape[0]-1,img.shape[1]-1-i] # 이미지의 끝부분 나머지를 삽입
                        break
                cube[idx][x,y,z]=img[i,j,k]  # 각 큐브에 이미지데이터 삽입
                z+=1

    return cube  # 큐브 리턴

def shuffle(arr,cube):      # 행렬을 사용해서 위치를 섞는 함수
    new_cube=[] # 반환할 새 큐브리스트
    temp=cube[:-1]  # 맨 마지막 나머지는 들어가면 안되므로 제외
    for data in temp:
        tmp=np.zeros([data.shape[0],data.shape[1],data.shape[2]],dtype=np.uint8) # data의 크기^3의 배열생성
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                for k in range(data.shape[2]):
                    array=np.array([i,j,k]).reshape(3,1) # i,j,k를 numpy 배열로 만들어줌
                    result=np.matmul(arr,array) # i,j,k와 입력받은 행렬 arr 곱하기

                    x=result[0][0]%data.shape[0]
                    y=result[1][0]%data.shape[1]
                    z=result[2][0]%data.shape[2]
                    # 각각의 x,y,z를 구하고 MOD N

                    tmp[x,y,z] = data[i,j,k] 
        new_cube.append(tmp) # new_cube에 tmp 추가

    new_cube.append(cube[-1]) # 원래 큐브의 맨 마지막 요소 넣기

    return new_cube  # 새 큐브 리턴

def combine(shape,cube): # 분할한 큐브를 다시 합치는 함수
    new=np.zeros([shape[0],shape[1],shape[2]],dtype=np.uint8)  # 이미지의 크기만큼 새 공간 생성    
    idx=0
    count=0
    x,y,z=0,0,0
    for i in range(new.shape[0]):
        for j in range(new.shape[1]):
            for k in range(new.shape[2]):                
                if z==cube[idx].shape[2]:
                    z=0
                    y+=1
                if y==cube[idx].shape[1]:
                    y=0
                    x+=1
                if x==cube[idx].shape[0]:
                    idx+=1
                    x,y,z=0,0,0
                    count=0
                    if idx==len(cube)-1:
                        for i in range(cube[-1].shape[0]):
                            new[new.shape[0]-1,new.shape[1]-1-i]=cube[-1][-1-i]
                        break
                new[i,j,k]=cube[idx][x,y,z]
                count+=1
                z+=1
                # 위 MakeCube와 비슷함
    return new 

if __name__=='__main__':
    img=cv2.imread('encrypt.png',1) # 이미지 읽어옵니다.
    cube=[]  # 각 큐브에 대한 데이터 담을 리스트

    cube = init(img,cube)
    cube = MakeCube(img,cube)

    arr=np.array([[1,1,1],[2,3,2],[1,1,2]])    #차분분석용

    arr2=np.linalg.inv(arr)      # arr의 역행렬
    arr2=np.array(arr2,dtype=int)
    
    cube = shuffle(arr,cube)   # 암호화할때
    #cube = shuffle(arr2,cube) # 복호화할때

    new_img=combine(img.shape,cube)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("cube_encrypt.png",new_img)  #파일 저장
    