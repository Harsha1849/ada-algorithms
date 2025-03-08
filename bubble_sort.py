n=int(input("Enter the number of elements: "))
print("Enter array elements one by one: ")
arr=[int(input()) for _ in range(n)]

swaps=0
comparision=0

for i in range(n-1):
    for j in range(n-1-i):
        comparision += 1

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swaps+=1

print("sorted array using bubble sort: ",arr)
print(f"Number of comparision: {comparision}")
print(f"Number of swaps: {swaps}")