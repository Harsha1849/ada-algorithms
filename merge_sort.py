import time  

n = int(input("Enter the number of elements: "))
print("Enter the elements one by one:")
arr = [int(input()) for _ in range(n)]  
start_time = time.time()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  
    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid])
    right, right_comparisons = merge_sort(arr[mid:])
    
    merged, merge_comparisons = merge(left, right)
    
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged, total_comparisons

def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            merged += [left[i]]  
            i += 1
        else:
            merged += [right[j]]  
            j += 1
    merged += left[i:] + right[j:]
    return merged, comparisons


sorted_arr, total_comparisons = merge_sort(arr)

end_time = time.time()
execution_time = end_time - start_time
print("Sorted Array using Merge Sort:", sorted_arr)
print(f"Total Comparisons: {total_comparisons}")
print(f"Execution Time: {execution_time:f} seconds")