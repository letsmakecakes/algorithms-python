# Python program to demonstrate array operations

# Importing array module
import array

# Creating an array
arr = array.array('i', [1, 2, 3, 4, 5])

# Function to display the array
def display_array(arr):
    print("Array:", list(arr))

# 1. Accessing an element (O(1))
print("Element at index 2:", arr[2])

# 2. Insertion (O(n))
arr.insert(2, 10)  # Insert 10 at index 2
print("After insertion at index 2:", list(arr))

# 3. Deletion (O(n))
arr.remove(10)  # Removes first occurrence of 10
print("After deletion:", list(arr))

# 4. Traversing an array (O(n))
print("Traversing the array:")
for element in arr:
    print(element, end=" ")
print()

# 5. Searching an element (O(n) for Linear Search)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

key = 3
index = linear_search(arr, key)
print(f"Element {key} found at index: {index}" if index != -1 else f"Element {key} not found")

# 6. Sorting an array (O(n log n))
sorted_arr = sorted(arr)  # Returns a new sorted list
print("Sorted array:", sorted_arr)

# Alternative: Using in-built sort method (O(n log n))
arr_list = list(arr)
arr_list.sort()
print("Array after in-place sorting:", arr_list)

# 7. Binary Search (O(log n)) [Requires sorted array]
import bisect

def binary_search(arr, key):
    index = bisect.bisect_left(arr, key)
    if index < len(arr) and arr[index] == key:
        return index
    return -1

key = 4
sorted_arr = sorted(arr)  # Ensure array is sorted before binary search
index = binary_search(sorted_arr, key)
print(f"Element {key} found at index: {index}" if index != -1 else f"Element {key} not found")
