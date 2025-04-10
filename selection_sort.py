n = int(input("Enter the number of elements: "))
print("Enter the elements one by one:")
arr = [int(input()) for _ in range(n)]

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array using Selection Sort:", arr)