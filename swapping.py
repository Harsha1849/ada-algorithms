def swapping(a,b):
    a=a+b
    b=a-b
    a=a-b

    return a,b

num1=10
num2=20

print("before swapping: ",num1,num2)
num1,num2=swapping(num1,num2)
print("after swapping: ",num1,num2)