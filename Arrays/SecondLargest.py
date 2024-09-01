# Second largest and second smallest element without sorting
"""
You have been given an array a of n unique non-negative integers.
Find the second largest and second smallest element from the array.

Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: n = 5, a = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
"""

##### SECOND LARGEST
def SecondLargest(arr):
    largest = arr[0]
    sec_largest = -1
    for i in range(0,len(arr)):
        if arr[i] > largest:
            sec_largest = largest
            largest = arr[i]
        elif arr[i] > sec_largest:
            sec_largest = arr[i]
    
    return sec_largest

##### SECOND SMALLEST
def SecondSmallest(arr):
    smallest = arr[0]
    sec_smallest = 100
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] < sec_smallest:
            sec_smallest = arr[i]
    
    return sec_smallest

a = [3,7,2,9,1]
# a = [1,2,3,4,5,6,7]
new_arr = []
new_arr.append(SecondLargest(a))
new_arr.append(SecondSmallest(a))
print(new_arr)  

###### COMBINING BOTH INTO ONE FUNCTION
def getSecondOrderElements(arr):
    new_arr =[]
    largest = arr[0]
    sec_largest = -1
    for i in range(0,len(arr)):
        if arr[i] > largest:
            sec_largest = largest
            largest = arr[i]
        elif arr[i] > sec_largest:
            sec_largest = arr[i]
    new_arr.append(sec_largest)    
    
    smallest = arr[0]
    sec_smallest = 100
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] < sec_smallest:
            sec_smallest = arr[i]
    new_arr.append(sec_smallest)
    return new_arr
        