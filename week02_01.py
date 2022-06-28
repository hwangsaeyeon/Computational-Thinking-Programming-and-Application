# 실행 후 data_describe('week_1_1.txt') 입력 
# 함수 #

def data_describe(fname):

    def load_data(fname):
        file=open(fname, encoding='UTF8')
        full=list() #txt파일을 리스트로 불러오기

        for line in file:
            full.append(line.strip())

            number=list() #숫자만 선별한 리스트
            for i in range (len(full)):
                if str(full[i]).isdigit():
                    number.append(int(full[i]))

            data=list() #1 이상의 숫자만 선별한 리스트 
            for i in range (len(number)):
                if number[i] >= 1:
                    data.append(number[i])
            
        file.close()
        return data

    def get_mean():
        hap=0
        cnt=0
        for i in range (len(data)):
            hap+=data[i]
            cnt+=1
        mean = (hap/cnt)
        
        return mean

    def get_std(mean):
        i=0
        j=0
        k=len(data)
        while (i<k):
            j+=(data[i]-mean)**2
            i+=1
        var=j/i
        import math
        return math.sqrt(var)

    def sort_values():
       for i in range (len(data)-1):
            for j in range (len(data)-1-i):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

    def get_median():
        median_idx=int((len(data)-1)/2)
        return data[median_idx]

    def get_max():
        max_val=0
        for i in range (len(data)):
            if max_val <= data[i]:
                max_val=data[i]
        return max_val

    def get_min():
        min_val=data[0]
        for i in range (len(data)):
            if min_val >= data[i]:
                min_val=data[i]
        return min_val



# 메인 #
    
    data = load_data(fname)
    mean = get_mean()
    std = get_std(mean)
    sort_values()
    median = get_median()
    max = get_max()
    min = get_min()

    print(f"""
    count = {len(data)}
    mean = {mean}
    median = {median}
    std = {std}
    max = {max}
    min = {min}
    """)
