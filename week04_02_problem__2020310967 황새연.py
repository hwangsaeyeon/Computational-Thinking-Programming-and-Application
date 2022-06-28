def ATM(N, nums):
    
    # return : min_sum # 인출 시간 합의 최소값
    
    ########### 함수 완성하기 ##########

   
    # 사람이 1명인 경우
    
    if N == 1:
        min_sum=nums[0]
    
    # 사람이 2명 이상인 경우
    # bubble sort 사용

    else:
        for i in range (N-1):
            for j in range (N-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    
    # 최소 인출시간 합 계산

    min_sum=0
    real_nums=0
    for k in range (N):
        real_nums+=nums[k] #cf) print('real',real_nums) 으로 실제 시간 과정 확인 가능
        min_sum+=real_nums #cf) print('min',min_sum) 으로 실제 시간의 합 과정 확인 가능
        

    #####################################
    return min_sum

### do not edit here ###
print('최소 시간:', ATM(5, [3, 1, 4, 3, 2]))

