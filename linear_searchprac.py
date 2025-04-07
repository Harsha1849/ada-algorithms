import time
n=int(input("Enter the number of elements: "))
print("Enter elements one by one: ")
arr=[int(input()) for _ in range()]
target=int(input("Enter element to be found: "))

found=False

start_time=time.time()

for i in range(n):
    if arr[i]==target:
        print(f"Element found at index {i}")
        found=True
        break

if not found:
    print("Element not found")

end_time=time.time()
execution_time=end_time-start_time
print("Time Taken to find: ", execution_time)