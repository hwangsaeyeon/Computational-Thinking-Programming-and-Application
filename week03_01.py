def score_average():
    """
    - 평균 성적 구하기
    - 반복문을 사용하여 성적을 입력 받는다. 
    - 'q' 입력시 종료
    - 조건문을 이용해 입력한 성적이 숫자가 아닌 경우('q' 제외) 오류 메세지는 출력하고 다시 성적을 입력 받는다.
    - 받을 수 있는 성적의 범위를 벗어난 경우 오류 메세지는 출력하고 다시 성적을 입력 받는다.

    """
    ######### 함수 완성하기 #########

    cnt=0
    sum=0
    print('성적을 입력하세요. :')
    while True:
        score=input('점수(0~100) : ')
        if score == 'q':
            if cnt==0: #secure coding
                print(' %d'%cnt,'과목 평균 성적 : %.1f'%sum)
                break
            else:
                print(' %d'%cnt,'과목 평균 성적 : %.1f'%(sum/cnt))
                break
        elif score.isnumeric() == False:
            print('%형식 오류%')
            continue
        elif int(score) < 0 or int(score) > 100:
            print('%범위 오류%')
            continue
        else:
            sum+=int(score)
            cnt+=1
            continue
        
    ######### ######### ######### 

##### do not edit here #####            
score_average()
