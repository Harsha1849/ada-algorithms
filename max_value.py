def find_Max(arr):
    max_value=arr[0]
    for i in range(1, len(arr)):
        if arr[i]>max_value:
            max_value=arr[i]
    return max_value

arr=[int(input("enter the elements: ")) for _ in range(int(input("enter the number of elements: ")))]
max_element=find_Max(arr)
print("Maximum element in array: ", max_element)