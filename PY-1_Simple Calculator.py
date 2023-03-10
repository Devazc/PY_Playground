#Project 1 is to build a simple functional calculator - 18/19

#1.Addition
def Add(n):

    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

#2.Subtraction
def Sub(num1,num2):
    return num1-num2

#3.Multiplication
def Mul(num1,num2):
    return num1*num2

#4.Division
def Div(num1,num2):
    return num1/num2

#Squareof
def Squareof(n):
    return n*n

print("Select the operator:\n"\
    "1.(+)Addition\n"\
    "2.(-)Subtraction\n"\
    "3.(x)Multiplication\n"\
    "4.(/)Division\n"\
    "5.Square of Given Number\n")

select = int(input("Enter the operator number 1,2,3,4,5: "))

if select == 1:

    n = input("Enter numbers:")
    print(Add(n))

if select == 5:
    n = int(input("Enter the Number = "))
    print(Squareof(n))    

elif select == 2 or 3 or 4:

    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))



    if select == 2:
        print(n1,"-",n2,"=",Sub(n1,n2))

    elif select == 3:
        print(n1,"*",n2,"=",Mul(n1,n2))

    elif select == 4:
        print(n1,"/",n2,"=",Div(n1,n2))




else:
    print("Invalid Operator/n"/
    "The Other Operators and Functions will be added soon, Thank you")
