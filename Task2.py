# Let's first overview the
# problem statement and understand the problem what we need to do.

# Task 2: Merge Two Sorted Arrays
# Write a program that merges two sorted arrays into a single sorted array.
# Example Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# So let's start the coding with creating two sorted arrays:)
array1 = [1, 3, 5]
array2 = [2, 4, 6]

# User-defined function to get the length of an array
def getLength(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

# Now I will create a merge function that merges the two sorted arrays without using
# built-in methods. 
def mergeSortedArrays(arr1, arr2):
    len1 = getLength(arr1)
    len2 = getLength(arr2)
    merged_array = [0] * (len1 + len2)
    i, j, k = 0, 0, 0

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            merged_array[k] = arr1[i]
            i += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
        k += 1

    # If there are remaining elements in arr1
    while i < len1:
        merged_array[k] = arr1[i]
        i += 1
        k += 1

    # If there are remaining elements in arr2
    while j < len2:
        merged_array[k] = arr2[j]
        j += 1
        k += 1

    return merged_array

# Custom printer to mimic ', '.join(map(str, merged_array))
def printArray(arr):
    n = getLength(arr)
    print("Merged Sorted Array:", "[", end="")
    for i in range(n):
        print(arr[i], end="")
        if i != n - 1:
            print(", ", end="")
    print("]")

# Now I will call the function and print the merged sorted array
merged_array = mergeSortedArrays(array1, array2)

# Now I will call the function and print the duplicates in ascending order
if getLength(merged_array) > 0:
    printArray(merged_array)
else:
    print("No elements found in the merged array.")
