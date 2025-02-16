def swapping(a,b):
    a=a+b
    b=a-b
    a=a-b

    return a,b

number1=10
number2=20

print("before swapping: ",number1,number2)
num1,num2=swapping(number1,number2)
print("after swapping: ",number1,number2)