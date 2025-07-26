# Let's first overview the
# problem statement and understand the problem what we need to do.

# Task 2: Merge Two Sorted Arrays
# Write a program that merges two sorted arrays into a single sorted array.
# Example Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# So let's start the coding with creating two sorted arrays:)
array1 = [1, 3, 5]
array2 = [2, 4, 6]
# Now I will create a merge function that merges the two sorted arrays without using
# built-in methods. 
def mergeSortedArrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    # If there are remaining elements in arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
        
    # If there are remaining elements in arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1  
        
    return merged_array

# Now I will call the function and print the merged sorted array
merged_array = mergeSortedArrays(array1, array2)

# Now I will call the function and print the duplicates in ascending order
if merged_array:
    print("Merged Sorted Array:","[", ', '.join(map(str, merged_array)), "]")
else:
    print("No elements found in the merged array.")
