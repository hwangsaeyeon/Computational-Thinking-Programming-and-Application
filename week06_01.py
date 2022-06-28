
def max_chicken(number_list):

    result=0
    n=len(number_list)

    dp1 = [0]*n
    dp2 = [0]*n
        
    dp1[0] = number_list[0] #첫번째 선택
    dp1[1] = number_list[0]

    dp2[0] = 0 #첫번째 선택X
    dp2[1] = number_list[1]
    
    for i in range(2,n-1): #마지막 선택X 
        dp1[i] = max(dp1[i-2]+number_list[i],number_list[i-1])
      
    for i in range(2, n):
        dp2[i] = max(dp2[i-2]+number_list[i],number_list[i-1])
            
    result = max(max(dp1),max(dp2))
    return result

def main():

  chicken_number = [2,3,4,1]

  print('먹을수 있는 닭다리 최대 개수: ', max_chicken(chicken_number))

if __name__ == "__main__":
  main()
