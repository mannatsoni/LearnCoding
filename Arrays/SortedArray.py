# Sort an Array : Selection Sort
"""Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
"""

arr = [1,5,10,7,0]
def Sorting(arr):
    for i in range(0,len(arr)):
        num=i+1
        for j in range(num,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

print(Sorting(arr))