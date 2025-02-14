def arithmetic(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return "error, division by zero" if num2==0 else num1/num2
    else:
        return "invalid operation"
    
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
operation=input("enter operation(+,-,*,/): ")
print("result=",arithmetic(num1,num2,operation))