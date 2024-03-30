# Python program for implementation of Selection
# Sort
import sys

A = [64, 64, 12, 22, 11]



# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i   0
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

        # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i], end=" , ")

# Complexity Analysis of Selection Sort
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:
#
# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
# space complexity = O(N)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly.
#
# Advantages of Selection Sort Algorithm
# Simple and easy to understand.
# Works well with small datasets.
# Disadvantages of the Selection Sort Algorithm
# Selection sort has a time complexity of O(n^2) in the worst and average case.
# Does not work well on large datasets.
# Does not preserve the relative order of items with equal keys which means it is not stable.

# FAQ
# Q1. Is Selection Sort Algorithm stable?
#
# The default implementation of the Selection Sort Algorithm is not stable. However, it can be made stable. Please see the stable Selection Sort for details.
#
# Q2. Is Selection Sort Algorithm in-place?
#
# Yes, Selection Sort Algorithm is an in-place algorithm, as it does not require extra space.