# Array Questions
## What is an Array?
Array is a data structure that is used to store similar data types in a programming language. In python, an array has been modified into a list which can store multiple data types at one time. 

While imagining an array in the computer memory, you can imagine same size boxes kept next to each other. Each box has one element.

You must define the space you need in advance and select those many boxes in the beginning.

### Q1 Finding the largest element in the array.
The logic is simple, you start from the first element and while looking through the array you check that element with each of the other element. As soon as you find an element larger than the current one, you replace the value with the larger one. Once the array is traverse, you simply return the largest variable.

### Q2 Finding second largest and second smallest element in an array.
Just define the largest element pointing to the first element of the array and define another variable say equal to -1.

We do this assuming that all values in the array are positive. 

Again, you may traverse through the array, as soon as a number is larger than your current large element, you replace the current larger element with the new one and your second largest element becomes your current largest element. On traversing the whole array you return your second largest element.

Same logic applies for second smallest element. Only, remember to start your for loop from the 1st index instead of zero. This will cover the use case of a sorted array as input. 