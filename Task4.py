# First of all understand the problem statement and the requirements.

# Task 4: Find Common Elements in Two Lists
# Write a function to find all common elements between two lists.
# Optimize to use a maximum of n + q comparisons, where n and q are the lengths of the two
# lists.
# Let's start coding to find common elements in two lists without using built-in methods.:

count_comparisons = 0

# Custom function to get length of a list
def getLength(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

# Custom function to check if an element is in a list
def custom_in(arr, target):
    global count_comparisons
    for i in range(getLength(arr)):
        count_comparisons += 1
        if arr[i] == target:
            return True
    return False

# Custom function to append to a list
def custom_append(arr, value):
    new_arr = [0] * (getLength(arr) + 1)
    for i in range(getLength(arr)):
        new_arr[i] = arr[i]
    new_arr[getLength(arr)] = value
    return new_arr

# Custom print for comma-separated values
def print_common_elements(arr):
    print("Common Elements:", end=" ")
    for i in range(getLength(arr)):
        print(arr[i], end="")
        if i != getLength(arr) - 1:
            print(", ", end="")
    print()

def find_common_elements(list1, list2):
    common_elements = []
    for i in range(getLength(list1)):
        element = list1[i]
        if custom_in(list2, element) and not custom_in(common_elements, element):
            common_elements = custom_append(common_elements, element)
    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
if getLength(common_elements) > 0:
    print_common_elements(common_elements)
    print(f"Total comparisons made: {count_comparisons}")
else:
    print("No common elements found between the two lists.")

# Example Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
# Output: Common Elements: 4, 5
# This code defines a function to find common elements between two lists
# without using built-in methods and prints the common elements if found.
# The function iterates through the first list and checks if each element is present in the second list,
# ensuring that duplicates are not added to the result.:)))))))))))))
# Created by Parkash Kumar
