def is_Prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num=int(input("Enter a number: "))

if is_Prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")