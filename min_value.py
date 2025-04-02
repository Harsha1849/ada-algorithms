import time
def find_Min(arr):
    min_value=arr[0]
    for i in range(1, len(arr)):
        if arr[i]<min_value:
            min_value=arr[i]
    return min_value


arr=[int(input("Enter the elements one by one: ")) for _ in range(int(input("enter the number of elements: ")))]
start_time=time.time()
min_element=find_Min(arr)
end_time=time.time()
execution_time=end_time-start_time

print("Minimum element in array: ", min_element)
print("time taken to find minimum element: ",execution_time)