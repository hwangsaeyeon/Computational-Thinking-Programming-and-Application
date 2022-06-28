### write inch2centi(), centi2inch(), choose_scale(), continues()
### make sure changeScale() iterate until user wants to stop


def get_number(message1):
    ### do not edit here ###
    num = input(message1)
    while not num.isdigit():
        num = input(message1)
    return int(num)


def centi2inch():
    # get value(centimeter), change it into inch, and print it
    
    print('-centimeter to inch')
    
    ### your code here ###
    
    value_cm=get_number('input number(centimeter) : ')
    centi2inch=round((value_cm/2.54),2)
    print('%.fcm -> %.2finch'%(value_cm,centi2inch)) 


def inch2centi():
    # get value(inch), change it into centimeter, and print it 

    print('-inch to centimeter')
    
    ### your code here ###
    
    value_inch=get_number('input number(inch) : ')
    inch2centi=round((value_inch*2.54),2)
    print('%.finch -> %.2fcm'%(value_inch,inch2centi))


def choose_scale(): 
    # get 1 or 2 as input (centi to inch or inch to centi)

    print('# centimeter to inch = 1')
    print('# inch to centimeter = 2')
    
    ### your code here ###
    
    sc=input('choose 1 or 2 : ')
    while not (sc == '1' or sc == '2'):
        sc=input('choose 1 or 2 : ')
        
    return sc


def continues():
    # ask to continue or not
    
    ### your code here ###
    
    while True:
        con=input('Wanna continue? (y/n)')
        if con == 'y':
            On = True
            break
        elif con == 'n':
            On = False
            break
        else:
            continue #secure coding
    return On


def changeScale():
    ### do not edit here ###
    sc = choose_scale()
    if sc == '1':
        centi2inch()
    elif sc == '2': 
        inch2centi()

# make sure changeScale() iterate until user wants to stop
def main():
    On = True
    while On: 
        changeScale()
        ### your code here ###
        On=continues()
        if On == True:
            continue
        elif On == False:
            break

main()
