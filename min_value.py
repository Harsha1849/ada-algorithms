def find_Min(arr):
    min_value=arr[0]
    for i in range(1, len(arr)):
        if arr[i]<min_value:
            min_value=arr[i]
    return min_value

arr=[int(input("enter the elements: ")) for _ in range(int(input("enter the number of elements: ")))]
min_element=find_Min(arr)
print("Minimum element in array: ", min_element)