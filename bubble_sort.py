import time
n=int(input("Enter the number of elements: "))
print("Enter array elements one by one: ")
arr=[int(input()) for _ in range(n)]

swaps=0
comparision=0

start_time=time.time()

for i in range(n-1):
    for j in range(n-1-i):
        comparision += 1

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swaps+=1

print("sorted array using bubble sort: ",arr)
print(f"Number of comparision: {comparision}")
print(f"Number of swaps: {swaps}")

end_time=time.time()
execution_time=end_time-start_time

print(f"time taken to sort using bubble sort: {execution_time}")