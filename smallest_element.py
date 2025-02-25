import time

n=int(input("Enter the number of elements in array: "))
print("Enter array elements: ")

arr=[int (input()) for _ in range(n)]

start_time=time.time()

smallest_element=min(arr)

end_time=time.time()

print("Smallest element in the array is: ",smallest_element)
execution_time=end_time-start_time
print(f"Time taken to find the smallest element is {execution_time:.2f} seconds")