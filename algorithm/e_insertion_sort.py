# Python program for implementation of Insertion Sort

# Function to do insertion sort
# def insertionSort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#
#         value = arr[i]
#         index = i
#         while index > 0 and value < arr[index-1]:
#             arr[index] = arr[index-1]
#             index-= 1
#         arr[index] = value
#
#
# # Driver code to test above
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# for i in range(len(arr)):
#     print("% d" % arr[i])

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]     N
[5,11,12,13,6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
#
# # This code is contributed by Mohit Kumra

# Time Complexity: O(N^2)
# Auxiliary Space: O(1)
#
# Complexity Analysis of Insertion Sort:
# Time Complexity of Insertion Sort
# The worst-case time complexity of the Insertion sort is O(N^2)
# The average case time complexity of the Insertion sort is O(N^2)
# The time complexity of the best case is O(N).
# Space Complexity of Insertion Sort
# The auxiliary space complexity of Insertion Sort is O(1)
#
# Characteristics of Insertion Sort
# This algorithm is one of the simplest algorithms with a simple implementation
# Basically, Insertion sort is efficient for small data values
# Insertion sort is adaptive in nature, i.e. it is appropriate for data sets that are already partially sorted.
# Frequently Asked Questions on Insertion Sort
# Q1. What are the Boundary Cases of the Insertion Sort algorithm?
#
# Insertion sort takes the maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
#
# Q2. What is the Algorithmic Paradigm of the Insertion Sort algorithm?
#
# The Insertion Sort algorithm follows an incremental approach.
#
# Q3. Is Insertion Sort an in-place sorting algorithm?
#
# Yes, insertion sort is an in-place sorting algorithm.
#
# Q4. Is Insertion Sort a stable algorithm?
#
# Yes, insertion sort is a stable sorting algorithm.
#
# Q5. When is the Insertion Sort algorithm used?
#
# Insertion sort is used when number of elements is small. It can also be useful when the input array is almost sorted, and only a few elements are misplaced in a complete big array.
