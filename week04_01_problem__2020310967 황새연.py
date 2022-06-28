def sosu(n):

    # return: True or False # 소수인지 아닌지 boolean type

    ######## 함수 완성하기 ########

    if n <= 1:
        return False #secure coding
    else:
        yaksu=0 #자신을 제외한 약수
        for i in range(1,n):
            if n%i == 0 :
                yaksu += 1
        if yaksu == 1:
            return True # 소수가 아님
        else:
            return False # 소수임
        
    ##############################

def sum_sosu(m,n):
    def loop(m,n,sum):

        # return loop(m,n,0): 꼬리재귀함수

        ######## 함수 완성하기 ########
        
        if m<n:
            if sosu(m) == True:
                return loop(m+1,n,sum+m)
            else:
                return loop(m+1,n,sum)
        else:
            return sum
            
        
        ###############################

    return loop(m,n,0)

### do not edit here ###
print('결과:',sum_sosu(1,10))
