import time

bList = [3,2,0,1,6,39,498,118,5,398,106,39,29,48,78,31,85,649,210]
N = len(bList)

def new_bList(List): #bList와 같은 값을 갖는 리스트 생성
    for i in range (N):
        List.append(bList[i])
    return List

def list1(bList): #loop을 끝까지 도는 버블 정렬 함수1
    start1=time.time()
    for i in range (N-1):
        for j in range (N-1-i):
            if bList[j] > bList[j+1]:
                bList[j], bList[j+1] = bList[j+1], bList[j]
    print(bList)
    print("time :", time.time() - start1)

def list2(bList): #loop을 멈추는 버블 정렬(재귀X) 함수2
    start2=time.time()
    for i in range (N-1):
        exchange = False
        for j in range (N-1-i):
            if bList[j] > bList[j+1]:
                bList[j], bList[j+1] = bList[j+1], bList[j]
                exchange = True
        if exchange == False:
            break
    print(bList)
    print("time :", time.time() - start2)
    
def list3(bList): #loop을 멈추는 버블 정렬(재귀O) 함수3
    start3=time.time()
    def bub(bList): 
        exchange = False
        for j in range (len(bList)-1):
            if bList[j] > bList[j+1]:
                bList[j], bList[j+1] = bList[j+1], bList[j]
                exchange = True
        if exchange == True:
            return bub(bList[:N])
        else:
            return print(bList)
    bub(bList)
    print("time :", time.time() - start3)

def Bubble(): #걸린 시간 비교 
    bList1=[]
    bList2=[]
    bList3=[]

    new_bList(bList1)
    new_bList(bList2)
    new_bList(bList3)

    list1(bList1)
    list2(bList2)
    list3(bList3)

#메인파트

Bubble()

bList=[] #리스트 초기화 
while True: #리스트에 정렬할 숫자를 입력받음
    num=input('리스트에 정렬할 숫자를 입력하세요(n또는 N은 stop):')
    if num == 'N' or num == 'n':
        N=len(bList)
        Bubble() #새로 생성된 리스트로 걸린 시간 비교
        break
    if  num.isdigit() == False:
        print('숫자가 아닙니다. 다시 입력하세요.')
        continue 
    else:
        bList.append(int(num))
        continue
