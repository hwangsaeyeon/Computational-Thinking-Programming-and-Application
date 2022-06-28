import random

class Account:
    bank = ("SKK은행")

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def account_number(self):
        self.account=''
        for i in range (13):
            self.account += str(random.randint(0,9))
            if i == 3 or i == 6:
                self.account += '-'
        return self.account



###### do not edit here ####### 
person = Account("철수", 1000)
print(person.name)
print(person.balance)
print(person.bank)
print(person.account_number())
