import time
n=int(input("Enter the number of elements: "))
print("Enter array elements in sorted order: ")
arr=[int(input()) for _ in range(n)]
target=int(input("Enter element to be found: "))

start_time=time.time()

found=False

for i in range(n):
    if arr[i]==target:
        print(f"Element found at {i}")
        found=True
        break
else:
    print("Element not found")

end_time=time.time()
execution_time=end_time-start_time
print("Time taken for execution: ", execution_time)