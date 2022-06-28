#### controller
class LottoController:  # 로또 컨트롤러
    def __init__(self, name):
        self.name=name
        
    
    def play(self):  # play 과정을 정하는 함수


        coin=5
        while True:
            in_n=(Reader.input_number())
            getnumber=Get_Number(self.name)
            ran_n=getnumber.get_number_selection()

            
            decision=Decision(self.name,ran_n,in_n,coin)
            decision.results()
            coin=decision.coin
            
            
            print('정답 숫자', decision.tnumber,',입력 숫자',decision.inumber,',맞춘 개수', decision.count)

            if decision.coin == 0: #점수가 0점인 경우 끝이 난다.
                print('Bankrupt!')
                break
            
            reader=Reader()
            msg='%s님(점수:%d점) 계속 하시겠습니까? 계속(1번)/그만(0번)'%(self.name,decision.coin)
            con=reader.ox(msg)
        
            if con == True:
                continue
            else:
                print('Exit!')
                break






        
                
#### model
class Get_Number:  # 로또 번호를 가져오는 클래스
    def __init__(self, name):
        self.name=name
        
    def get_number_selection(self):  # 랜덤 번호가 담긴 리스트 생성 함수
        import random

        numbers=[]
        for _ in range (3):
            get=random.randrange(1,16)
            numbers.append(get)
        
        return numbers










    
class Decision:  # 결과 결정하는 클래스
    def __init__(self, name, tnumber, inumber, coin):
        self.__name=name
        self.__tnumber=tnumber
        self.__inumber=inumber
        self.__coin=coin
        self.__count=0
        
       
        
    @property
    def tnumber(self):  #로또 번호 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self.__tnumber
    
    @property
    def inumber(self):  #참가자가 작성한 번호 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self.__inumber
    
    @property
    def coin(self):  #현재 코인 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self.__coin
    
    @property
    def count(self):  #몇 개 맞췄는지에 대한 카운트 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self.__count
    
    def results(self):  #입력한 번호와 로또 번호가 몇 개 일치하는지 계산하는 함수  
        for j in range (3):
            i=0
            while i < 3:
                if self.__inumber[j] == self.__tnumber[i]:
                    self.__count+=1
                    break
                i+=1    

        if self.__count == 3:
            self.__coin += 5
        elif self.__count == 2:
            self.__coin += 3
        else:
            self.__coin -= 1
        










class Reader:  #참가자 입력정보 클래스
    @staticmethod
    def get_name():  #참가자 이름 입력 받아오는 함수, return 뒤에 올 코드를 완성하시오.
        return input('플레이어의 이름을 입력하세요:')
    
    @staticmethod
    def ox(message):  #참가자가 계속할건지 종료할건지 리턴하는 함수
        response = input(message)
        while not (response == '1' or response == '0'):
            response = input(message)

        if response == '1':
            return True   
        else:
            return False
            
    @staticmethod
    def input_number():  #참가자가 입력하는 번호를 리스트로 리턴하는 함수

        numbers=[]
        for i in range (1,4):
            inum=int(input('%d번째 숫자 입력:'%i))
            if inum < 1 or inum > 15:
                print('선택할 수 없는 번호입니다.')
                inum=int(input('%d번째 숫자 입력:'%i))
            numbers.append(inum)
        
        return numbers
    
    
#### main
######## do not edit here ########
def main():
    reader = Reader()
    name = reader.get_name()
    
    lottocontroller = LottoController(name)
    lottocontroller.play()
    
if __name__ == "__main__":
    main()
