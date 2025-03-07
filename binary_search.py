import time

n=int(input("Enter the number of elements in array: "))
print("Enter sorted array elements one by one: ")
arr=[int(input()) for _ in range(n)]
target=int(input("Enter element to be found: "))

left,right=0,n-1
found=False

start_time=time.time()

while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(f"Element found at index {mid}")
        found=True
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1

if not found:
    print("Element not found")

end_time=time.time()
execution_time=end_time-start_time
print(f"Time taken to find element: {execution_time}")