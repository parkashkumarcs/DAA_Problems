# Before we do start the coding in python let's first overview the
# problem statement and understand precisely what we need to do.
# Problem1:
# Task 1: Find Duplicates in an Unsorted Array
# Write a program to identify and print all duplicate elements in an unsorted array.
# Example Input: [4, 2, 7, 2, 5, 4]
# Output: Duplicates: 2, 4

# So let's start the coding with creating an array:)

myArray = [4, 2, 7, 2, 5, 4]

# Storing the length of the array
arrLength = len(myArray);
print("Length of the array is: ", arrLength);

# Now I will create a duplicate funcntion in which I will
# find the duplicates in the array and print them without using 
# built-in methods.
def findDuplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Now I will call the function and print the duplicates in ascending order
duplicates = findDuplicates(myArray)
if duplicates:
    print("Duplicates:", ', '.join(map(str, sorted(duplicates))))
else:
    print("No duplicates found in the array.")
