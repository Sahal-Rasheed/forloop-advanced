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
    if operator=="1":
        replace1="Addition"
        operation=a+b
    if operator=="2":
        if a>b:
            replace1="Subtraction"
            operation=a-b
        else:
            print("\nCannot subtract the First number is less than the Second number")
            flag=False
    if operator=="3":
        if a!=0 and b!=0:
            replace1="Multiplication"
            operation=a*b
        else:
            print("\nCannot multiply because one of the number is 0")
            flag=False
    if operator=="4":
        if b!=0:
            replace1="Division"
            operation=a//b
        else:
            print("\nCannot divide because one of the number is 0")
            flag = False
    if operator=="5":
        replace1="Modulus"
        operation=a%b
    if flag==True:
        print("\nThe result of" ,replace1, "of" ,a, "and" ,b, "is" ,operation)

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


