
from bs4 import BeautifulSoup #bs4에서 BeautifulSoup 함수를 import
from urllib.request import Request, urlopen #urllib에서 urlopen, Request 함수를 import
import pandas as pd #pandas를 import해서 pd로 사용
import time #소요시간, 시작시간, 완료시간 print하기 위함



def Crawling(url): #크롤링 함수

        company=[] #기업명 리스트
        title=[] #제목 리스트
        score=[] #별점 리스트
        salary=[] #평균연봉 리스트
        recommend=[] #직원추천 리스트


        for n in range (1,8): #page 1~7

                
                URL=url+"&page="+str(n) #페이지에 따라 url 변경
                req = Request(URL ,headers={'User-Agent':'Mozilla/5.0'}) #크롤링할 수 있도록 request
                openUrl = urlopen(req).read() #req 호출해 url 연다
                soup = BeautifulSoup(openUrl, 'html.parser') #BeautifulSoup 이용해 구문 분석

                #기업명 
                company_text = soup.find_all('button',{'class':{'btn_open'}})
                #('태그명',{'속성명1':{'값1'}}) 찾기
                #soup에서 <button class="btn_open"></button> 출력
                for i in company_text: #compnay_text 요소 
                        company.append(i.get_text()) #company 리스트에 기업명만 append


                #제목
                title_text = soup.find_all('a',{'class':{'posting_name'}})
                for i in title_text: #title_text 요소
                        title.append(i.get_text()) #title 리스트에 제목만 append

                #별점, 평균연봉, 직원추천

                info=[]
                #별점, 평균연봉, 직원추천을 append할 info 리스트
                #리뷰가 10개 미만인 기업은 별점, 평균연봉, 직원추천을 open하지 않으므로, 혹은 평균연봉을 제공하지 않는 기업이 있으므로 따로 리스트 생성

                info_text = soup.find_all('div',{'class':{'jp_data_set'}}) #별점, 평균연봉, 직원추천을 모두 크롤링
                for i in range(len(info_text)): #info_text 길이만큼 반복
                        data=info_text[i].get_text().strip().split('\n|\n') #info_text에서 별점, 평균연봉, 직원추천을 하나의 리스트로 data에 저장. 공백 제거 및 \n|\n을 기준으로 split
                        info.append(data) #info 리스트에 data append


                for i in range(len(info)): #info 리스트 길이만큼 반복
                        if len(info[i]) == 3: #별점, 평균연봉, 직원추천이 모두 존재 
                                score.append(info[i][0]) #score 리스트에 별점 append
                                salary.append(info[i][1]) #salary 리스트에 평균연봉 append
                                recommend.append(info[i][2]) #recommend 리스트에 직원추천 append
                        elif len(info[i]) == 2: #별점, 직원추천만 존재
                                score.append(info[i][0]) 
                                salary.append('제공X')
                                recommend.append(info[i][1])
                        elif len(info[i]) == 1: #별점, 평균연봉, 직원추천 모두 제공X
                                score.append('제공X')
                                salary.append('제공X')
                                recommend.append('제공X')




                                
        #pandas, 딕셔너리 사용해서 위 리스트들을 보기 쉽게 정리
        result = pd.DataFrame({'기업명': company,
                                '제목': title,
                                '별점': score,
                                '평균연봉': salary,
                                '직원추천': recommend
                                 })


        return result 





#main

while True:
        jobplanet=input('웹사이트 주소:' ) #https://www.jobplanet.co.kr/job_postings/search?_rs_act=browse&_rs_con=job&_rs_element=job_postings&occupation_level2_ids%5B%5D=11613 입력

        start=time.localtime(time.time()) #시작시간 
        st_check=time.time() #소요시간 계산 위한 시작시간 체크
        save=time.strftime('%Y%m%d%H%M.csv',start) #출력파일 이름은 현재 시간으로
        #time.strftime('포맷',시간객체)
        
        rst=Crawling(jobplanet) #함수에 url 입력

        #csv 파일로 저장
        rst.to_csv(save) 
        print('%s'%(save),'파일에 크롤링 결과가 저장되었습니다.')
        
        end=time.localtime(time.time()) #완료시간 
        end_check=time.time() #소요시간 계산 위한 완료시간 체크
        
        print('소요시간: %d초'%(end_check-st_check)) #소요시간 계산 
        print(time.strftime('시작시간: %Y년 %m월 %d일 %H시 %M분 %S초', start))
        print(time.strftime('완료시간: %Y년 %m월 %d일 %H시 %M분 %S초', end))

        con=input('계속하시겠습니까? ') #'네' 입력시 처음으로 되돌아감. 이외 입력시 종료
        if con == '네':
              continue
        else:
                break


