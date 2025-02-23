def is_prime_range(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i==0:
            return False
    return True

start=int(input("Enter start point: "))
end=int(input("Enter end point: "))

print(f"Prime numbers between {start} and {end} are: ")

for num in range(start, end+1):
    if is_prime_range(num):
        print(num, end=" ")

print()