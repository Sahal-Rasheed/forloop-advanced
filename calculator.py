flag=True
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("These are the operators you can choose :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    replace1="Addition"
    operation=a+b
if operator=="2":
    if a>b:
        replace1="Subtraction"
        operation=a-b
    else:
        print("Cannot subtract the First number is less than the Second number")
        flag=False
if operator=="3":
    replace1="Multiplication"
    operation=a*b
if operator=="4":
    replace1="Division"
    operation=a//b
if operator=="5":
    replace1="Modulus"
    operation=a%b
if flag==True:
    print("The result of" ,replace1, "of" ,a, "and" ,b, "is" ,operation)


