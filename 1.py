print("*************CALCULATOR****************")
def calc():
    flag = True
    a=int(input("\nEnter the first number :\t"))
    b=int(input("\nEnter the second number :\t"))
    print("\nThese are the operators you can choose :\t")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    operator=input("\nPlease choose an option from these (1,2,3,4,5):\t")
    def add(a,b):
        return(a+b)
    if operator=="1":
        result=add(a,b)
        print(result)
        replace1="Addition"
    def sub(a,b):
        return(a-b)
    if operator=="2":
        if a>b:
            result=sub(a,b)
            print(result)
            replace1="Subtraction"
        else:
            print("\nCannot subtract the First number is less than the Second number")
            flag=False
    def mul(a,b):
        return(a*b)
    if operator=="3":
        if a!=0 and b!=0:
            replace1="Multiplication"
            result=mul(a,b)
            print(result)
        else:
            print("\nCannot multiply because one of the number is 0")
            flag=False
    def div(a,b):
        return(a//b)
    if operator=="4":
        if b!=0:
            replace1="Division"
            result=div(a,b)
            print(result)
        else:
            print("\nCannot divide because one of the number is 0")
            flag = False
    def mod(a,b):
        return(a%b)
    if operator=="5":
        if b!=0:
            replace1="Modulus"
            result=mod(a,b)
            print(result)
        else:
            print("\nCannot find reminder because one of the 2nd number is 0")
            flag = False
    if flag==True:
        print("\nThe result of" ,replace1, "of" ,a, "and" ,b, "is" ,result)

    again()

def again():
    c_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.\t''')
    if c_again.upper() == "Y":
        calc()
    elif c_again.upper() == "N":
        print("\n********THANK YOU FOR USING OUR CALCULATOR*******")
    else:
        again()
calc()


