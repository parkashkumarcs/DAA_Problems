# Before we do start the coding in python let's first overview the
# problem statement and understand precisely what we need to do.

# Task 1: Find Duplicates in an Unsorted Array
# Write a program to identify and print all duplicate elements in an unsorted array.
# Example Input: [4, 2, 7, 2, 5, 4]
# Output: Duplicates: 2, 4

# So let's start the coding with creating an array:)

myArray = [4, 2, 7, 2, 5, 4]

# Storing the length of the array
def getLength(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

arrLength = getLength(myArray);
print("Length of the array is: ", arrLength);

# Now I will create a duplicate funcntion in which I will
# find the duplicates in the array and print them without using 
# built-in methods.
def findDuplicates(arr):
    duplicates = [0] * 100  # assuming array values < 100
    dupIndex = 0
    for i in range(getLength(arr)):
        isDuplicate = False
        for j in range(i + 1, getLength(arr)):
            if arr[i] == arr[j]:
                alreadyFound = False
                for k in range(dupIndex):
                    if duplicates[k] == arr[i]:
                        alreadyFound = True
                        break
                if not alreadyFound:
                    duplicates[dupIndex] = arr[i]
                    dupIndex += 1
                break
    # Create result array of exact size
    result = [0] * dupIndex
    for i in range(dupIndex):
        result[i] = duplicates[i]
    return result

# Custom sorting function (ascending)
def sortArray(arr):
    n = getLength(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

# Custom join-like printer
def printDuplicates(arr):
    n = getLength(arr)
    print("Duplicates: ", end="")
    for i in range(n):
        print(arr[i], end="")
        if i != n - 1:
            print(", ", end="")
    print()

# Now I will call the function and print the duplicates in ascending order
duplicates = findDuplicates(myArray)
if getLength(duplicates) > 0:
    printDuplicates(sortArray(duplicates))
else:
    print("No duplicates found in the array.")
