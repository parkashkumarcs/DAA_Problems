# First of all understand the problem statement and the requirements.

# Task 4: Find Common Elements in Two Lists
# Write a function to find all common elements between two lists.
# Optimize to use a maximum of n + q comparisons, where n and q are the lengths of the two
# lists.
# Let's start coding to find common elements in two lists without using built-in methods.:
count_comparisons = 0
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            # Increment the comparison count
            global count_comparisons
            count_comparisons += 1
            common_elements.append(element)
    return common_elements
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
if common_elements:
    print("Common Elements:", ', '.join(map(str, common_elements)))
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