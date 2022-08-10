a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("These are the operators you can choose :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operators=(input("Please choose an option from these (1,2,3,4,5):"))
if operator==1:
    print("The sum of two numbers is", a+b)
if operator=="2":
    print("The difference of two numbers is", a-b)
if operator=="3":
    print("The product of two numbers is", a*b)
if operator=="4":
    print("The division of two numbers is", a/b)
if operator=="5":
    print("The modulus of two numbers is", a%b)
if operator>5:
    print("not valid")



