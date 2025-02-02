# Optimized Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        flag = 0

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if (flag == 0):
            break


# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    print(arr)
    # for i in range(len(arr)):
    #     print("%d" % arr[i], end=" ")


# Time Complexity: O(N2)
# Auxiliary Space: O(1)
#
# Advantages of Bubble Sort:
# Bubble sort is easy to understand and implement.
# It does not require any additional memory space.
# It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
# Disadvantages of Bubble Sort:
# Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
# Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set.
# It can limit the efficiency of the algorithm in certain cases.

# FAQ
# What is the Boundary Case for Bubble sort?
# Bubble sort takes minimum time (Order of n) when elements are already sorted. Hence it is best to check if the array is already sorted or not beforehand, to avoid O(N2) time complexity.
#
# Does sorting happen in place in Bubble sort?
# Yes, Bubble sort performs the swapping of adjacent pairs without the use of any major data structure. Hence Bubble sort algorithm is an in-place algorithm.
#
# Is the Bubble sort algorithm stable?
# Yes, the bubble sort algorithm is stable.
#
# Where is the Bubble sort algorithm used?
# Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. In computer graphics, it is popular for its capability to detect a tiny error (like a swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n).
#
# Example: It is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to the x-axis), and with incrementing y their order changes (two elements are swapped) only at intersections of two lines.