# Find the largest element in a given array
"""
Problem statement
Given an array arr of size n find the largest element in the array.

Example:
Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
"""

arr = [5,8,3,2,1,9]

# Brute force way to solve this is by using the sorted function from python and returning the last element.
def LargestElement_BF(arr):
    arr = sorted(arr)
    return arr[-1]
print(LargestElement_BF(arr))

def LargestElement(arr):
    largest = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

print(LargestElement(arr))    
        
    
