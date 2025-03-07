n=int(input("Enter the number of elements in array: "))
print("Enter sorted array elements: ")
arr=[int(input()) for _ in range(n)]
target=int(input("Enter element to be found: "))

found=False

for i in range(n):
    if arr[i]==target:
        print(f"Element found at index {i}")
        found=True
        break

if not found:
    print("Element not found")