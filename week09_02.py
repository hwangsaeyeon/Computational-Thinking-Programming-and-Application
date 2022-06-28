import numpy as np

def get_integer(message, a, b):
    n = input(message)
    if b == None:
        while not((n[0]=='-' and n[1:].isdigit()) or n.isdigit() and int(n)>=a):
            n = input(message)
    else:
        while not((n[0]=='-' and n[1:].isdigit()) or n.isdigit() and int(n)>=a and int(n)<=b):
            n = input(message)
    return int(n)




                  
def print_score(score):  #학생 점수 출력 기능
    
    print('\n학생 수는 %d명 입니다.'%n)
    score_who=get_integer("학생의 번호를 입력하세요: ", 1, n)
    print(score_who,'의 점수 : ',score[(score_who)-1])



    

def fix_score(score):  #학생의 점수 수정 기능
    
    print('\n학생 수는 %d명 입니다.'%n)
    fix_who=get_integer("학생의 번호를 입력하세요: ", 1, n)
    print(fix_who,'의 점수 : ',score[(fix_who)-1])
    print('수정할 점수를 입력하세요.\n-1을 입력하면 점수는 유지됩니다.')

    subject=['국어','수학','영어','한국사']
    for i in range (len(subject)):
        msg=('%s 점수 : %s의 점수 : '%(subject[i],subject[i]))
        new_score=get_integer(msg,0,100)
        if new_score == -1:
            pass
        else:
            score[(fix_who)-1,i] = new_score



            

def stats_subject(score):  #과목별 평균, 분산 보기 기능

    kor = np.zeros((1,n)) #국어값 numpy
    mat = np.zeros((1,n)) #수학값 numpy
    eng = np.zeros((1,n)) #영어값 numpy
    his = np.zeros((1,n)) #한국사값 numpy
    
    for i in range(n):
        kor[0,i]+=score[i,0]
        mat[0,i]+=score[i,1]
        eng[0,i]+=score[i,2]
        his[0,i]+=score[i,3]

    print('\n국어평균 : %.2f 국어분산 : %.2f'%(np.mean(kor),np.var(kor)))
    print('수학평균 : %.2f 수학분산 : %.2f'%(np.mean(mat),np.var(mat)))
    print('영어평균 : %.2f 영어분산 : %.2f'%(np.mean(eng),np.var(eng)))
    print('한국사평균 : %.2f 한국사분산 : %.2f'%(np.mean(his),np.var(his)))




    
                  
def stats_student(score):  #학생별 평균, 분산 계산 기능

    st=list() #학생들의 번호를 기억할 리스트
    real_st=list() #중복된 번호가 없는 리스트
    
    
    print('\n0을 입력하면 학생 번호 입력이 종료됩니다.')

    while True:
        student=get_integer('학생의 번호를 입력하세요. :',0,n)
        if student == 0:
            break
        else:
            st.append(student)

    for i in range (len(st)):
        if st[i] in st[:i]: #중복된 번호 제거
            pass
        else:
            print(st[i],'의 점수 : ',score[(st[i])-1])
            real_st.append(st[i])

    s=len(real_st)
    
    kor = np.zeros((1,s)) #국어값 numpy
    mat = np.zeros((1,s)) #수학값 numpy
    eng = np.zeros((1,s)) #영어값 numpy
    his = np.zeros((1,s)) #한국사값 numpy
    
    for i in range(s):
        kor[0,i]+=score[i,0]
        mat[0,i]+=score[i,1]
        eng[0,i]+=score[i,2]
        his[0,i]+=score[i,3]

    print('국어평균 : %.2f 국어분산 : %.2f'%(np.mean(kor),np.var(kor)))
    print('수학평균 : %.2f 수학분산 : %.2f'%(np.mean(mat),np.var(mat)))
    print('영어평균 : %.2f 영어분산 : %.2f'%(np.mean(eng),np.var(eng)))
    print('한국사평균 : %.2f 한국사분산 : %.2f'%(np.mean(his),np.var(his)))

    
    
    
    
    
    
    
    
    
    
    
    
                  

##### do not edit here #####
n = get_integer("학생 수를 입력하세요. : ", 1, None)
                  
score = np.random.randint(0, 101, (n, 4))
                  
while True:
    print("\n<메뉴>")
    print("1. 학생의 점수 출력")
    print("2. 학생의 점수 수정")              
    print("3. 과목별 평균, 분산 보기")              
    print("4. 학생별 평군, 분산 계산")              
    print("0. 종료")              
    ch = get_integer("할 일의 번호를 선택하세요. : ", 0, 4)
                  
    if ch == 1:
        print_score(score)
    elif ch == 2:
        fix_score(score)
    elif ch == 3:
        stats_subject(score)
    elif ch == 4:
        stats_student(score)
    else:
        break
