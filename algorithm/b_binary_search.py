# array should already be sorted
# continuosly divide the array in half and search for the element
# In this way time can be saved

arr = [10, 23, 45, 70, 90, 100, 111]
start = 0
end = len(arr) - 1
key = int(input())
while start <= end:
    mid = (start + end) // 2
    if key == arr[mid]:
        print("search found")

    if key > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1

