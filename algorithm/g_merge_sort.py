def merge(arr, start, mid, end):
    temp = [None] * (end - start + 1)

    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    k = 0

    for i in range(start, end + 1):
        arr[i] = temp[k]
        k += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)


if __name__ == "__main__":
    n = 8
    arr = [5, 20, 30, 45, 10, 25, 28, 40]
    mergeSort(arr, 0, n - 1)
    for i in range(len(arr)):
        print(arr[i], end=" ")

# Complexity Analysis of Merge Sort
# Time Complexity: O(N log(N)),  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
#
# T(n) = 2T(n/2) + θ(n)
#
# The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of the Master Method and the solution of the recurrence is θ(Nlog(N)). The time complexity of Merge Sort isθ(Nlog(N)) in all 3 cases (worst, average, and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
#
# Auxiliary Space: O(N), In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required for merge sort.
#
# Applications of Merge Sort:
# Sorting large datasets: Merge sort is particularly well-suited for sorting large datasets due to its guaranteed worst-case time complexity of O(n log n).
# External sorting: Merge sort is commonly used in external sorting, where the data to be sorted is too large to fit into memory.
# Custom sorting: Merge sort can be adapted to handle different input distributions, such as partially sorted, nearly sorted, or completely unsorted data.
# Inversion Count Problem
# Advantages of Merge Sort:
# Stability: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
# Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.
# Parallelizable: Merge sort is a naturally parallelizable algorithm, which means it can be easily parallelized to take advantage of multiple processors or threads.
# Drawbacks of Merge Sort:
# Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process.
# Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
# Not always optimal for small datasets: For small datasets, Merge sort has a higher time complexity than some other sorting algorithms, such as insertion sort. This can result in slower performance for very small datasets.