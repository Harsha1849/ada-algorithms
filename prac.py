import time
n=int(input("Enter the number of elements: "))
print("Enter array elements one by one: ")
arr=[int(input()) for _ in range(n)]

comparisions=0
swaps=0
start_time=time.time()

for i in range(n-1):
    for j in range(n-1-i):
        comparisions+=1
    
    if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swaps+=1

print(f"Sorted array: {arr}")
print("Total comparisions: ",comparisions)
print("Total Swaps: ",swaps)