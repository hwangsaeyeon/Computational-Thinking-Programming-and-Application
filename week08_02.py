# 채점기준
# 총점을 90점으로 두고, 메서드 당 10점. 

class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator #분자
        self.denominator=denominator #분모
        

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def negate(self):
        return MyFraction(-self.numerator, self.denominator)

    def inverse(self):
        return MyFraction(self.denominator, self.numerator)

    def reduction(self):
        
        reduc=list()
        m=max(self.numerator,self.denominator)
        for i in range (1,m+1):
            if (self.numerator%i==0) and (self.denominator%i==0):
                reduc.append(i)
                
        gcm=max(reduc) #gcm=최대공약수
        self=MyFraction(self.numerator//gcm, self.denominator//gcm)
        
        return self

    def __add__(self, frac):

        if isinstance(frac, int) is True: #frac이 정수일 때, 유리수로 바꿔주는 작업
             frac=MyFraction(frac,1)
             
        numerator=self.numerator*frac.denominator+self.denominator*frac.numerator
        denominator=self.denominator*frac.denominator
        
        
        return MyFraction(numerator, denominator).reduction()

    def __sub__(self, frac):

        if isinstance(frac, int) is True: #frac이 정수일 때, 유리수로 바꿔주는 작업
             frac=MyFraction(frac,1) 
        
        return self.__add__(frac.negate())

    def __mul__(self, frac):
        
        if isinstance(frac, int) is True: #frac이 정수일 때, 유리수로 바꿔주는 작업
             frac=MyFraction(frac,1) 
        
        numerator=self.numerator*frac.numerator
        denominator=self.denominator*frac.denominator
        
        
        return MyFraction(numerator, denominator).reduction()


    def __truediv__(self, frac):

        if isinstance(frac, int) is True: #frac이 정수일 때, 유리수로 바꿔주는 작업
             frac=MyFraction(frac,1) 
        
        return self.__mul__(frac.inverse())


### do not edit here
if __name__ == '__main__':
    a = MyFraction(1,2)
    b = MyFraction(13,15)
    x = a + b
    print(f'x={x}, a={a}, b={b}')

    c = x - a
    d = x - 1
    y = c / d
    print(f'y={y}, c={c}, d={d}')	
