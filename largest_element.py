import time

n=int(input("Enter the number of elements in the array: "))
print("Enter array elements: ")
arr=[int(input()) for _ in range(n)]

start_time=time.time()

max_element=max(arr)

end_time=time.time()

print(f"Largest element in the array is: {max_element}")
execution_time=end_time-start_time
print(f"Time taken to find the largest element is {execution_time:.2f} seconds")