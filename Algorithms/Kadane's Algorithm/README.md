# Kadane's Algorithm - Maximum Subarray Sum

## Introduction
Kadane's Algorithm is a dynamic programming technique used to find the maximum sum of a contiguous subarray in a given one-dimensional array of numbers. It is highly efficient with a time complexity of **O(n)**, making it ideal for solving the Maximum Subarray Problem.

## Problem Statement
Given an array `arr` of size `n`, find the contiguous subarray (containing at least one number) that has the largest sum and return that sum.

### Example 1:
#### Input:
```plaintext
arr = [-2,1,-3,4,-1,2,1,-5,4]
```
#### Output:
```plaintext
6
```
#### Explanation:
The contiguous subarray `[4, -1, 2, 1]` has the maximum sum of `6`.

## Algorithm
1. Initialize two variables:
   - `max_current` to store the maximum sum ending at the current position.
   - `max_global` to store the maximum sum found so far.
2. Set both `max_current` and `max_global` to the first element of the array.
3. Iterate through the array starting from the second element.
   - Update `max_current` as the maximum between the current element and `max_current + current_element`.
   - Update `max_global` if `max_current` is greater than `max_global`.
4. Return `max_global` as the result.

## Implementation
### Python Code:
```python
def kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

# Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane(arr))  # Output: 6
```

## Complexity Analysis
- **Time Complexity:** `O(n)` - Since we iterate through the array once.
- **Space Complexity:** `O(1)` - No extra space is used apart from variables.

## Applications
- Used in stock market analysis to find the best time to buy and sell stocks.
- Signal processing for finding high-energy segments.
- Used in image processing and computer vision for feature extraction.
- A fundamental technique in dynamic programming problems.

## References
- [Wikipedia - Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [GeeksforGeeks - Kadane's Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)