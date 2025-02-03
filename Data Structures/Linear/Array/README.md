# Arrays

## Introduction
An **array** is a data structure that stores a fixed-size sequential collection of elements of the same type. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

## Features of Arrays
- Fixed size (in most programming languages)
- Elements stored in contiguous memory locations
- Can store multiple elements of the same data type
- Supports random access to elements using an index
- Efficient in terms of time complexity for accessing elements

## Types of Arrays
1. **One-Dimensional Array (1D Array)**
   - A linear list of elements.
   - Example: `[1, 2, 3, 4, 5]`
   
2. **Two-Dimensional Array (2D Array)**
   - An array of arrays, forming a matrix-like structure.
   - Example:
     ```plaintext
     [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
     ```

3. **Multi-Dimensional Arrays**
   - Arrays with more than two dimensions, often used in complex mathematical computations.

## Common Operations on Arrays and Their Complexities
### 1. Declaration and Initialization
#### Python:
```python
arr = [1, 2, 3, 4, 5]
```


### 2. Accessing Elements (O(1))
#### Python:
```python
print(arr[2])  # Output: 3
```


### 3. Traversing an Array (O(n))
#### Python:
```python
for i in arr:
    print(i)
```


### 4. Insertion and Deletion (O(n))
- **Insertion** involves adding a new element at a specified index (requires shifting elements).
- **Deletion** involves removing an element and shifting elements accordingly.

### 5. Searching an Element
#### Linear Search (O(n))
```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
```

#### Binary Search (O(log n)) [Only for Sorted Arrays]
```python
import bisect
index = bisect.bisect_left(arr, key)
```

### 6. Sorting an Array (O(n log n))
#### Python:
```python
arr.sort()
```


## Advantages of Arrays
- Fast and efficient access to elements using an index (O(1)).
- Useful for implementing other data structures like stacks and queues.

## Disadvantages of Arrays
- Fixed size (in static arrays, memory allocation is done at compile time).
- Insertion and deletion operations are costly because of shifting elements (O(n)).

## Applications of Arrays
- Storing and accessing large datasets
- Used in search and sorting algorithms
- Implementing matrices in mathematical computations
- Used in image processing and game development

## Conclusion
Arrays are a fundamental data structure used in almost every programming language. Understanding their operations, complexities, advantages, and limitations is essential for efficient problem-solving in computer science.

---

### References
- [GeeksforGeeks - Arrays](https://www.geeksforgeeks.org/array-data-structure/)
- [Wikipedia - Arrays](https://en.wikipedia.org/wiki/Array_data_structure)

