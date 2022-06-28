def binary_search(arr, score):

    # 코드를 작성하세요

    # arr 버블 정렬
    for i in range (len(arr)-1):
        for j in range (len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 이진 검색
    start=0
    end=len(arr)-1
    while start <= end :
        
        mid=(start+end)//2
        
        if arr[mid] == score:
            break
        elif arr[mid] < score:
            start=mid+1
        elif arr[mid] > score:
            end=mid-1
            
    rank=len(arr)-mid
    return rank

# 파일 불러오기 코드 작성

file=open('score.txt','r')
scores=list()
for line in file:
    scores.append(float(line.strip()))
file.close()

# 메인 코드 

my_score = 81
rank = binary_search(scores, my_score)
print(f'{my_score}점은 {rank}등 입니다')

