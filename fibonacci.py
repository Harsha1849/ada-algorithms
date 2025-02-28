def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a, end=" ")
        a,b=b,a+b

num=int(input("Enter the series range: "))
print("Fibonacci Series: ")
fibonacci(num)