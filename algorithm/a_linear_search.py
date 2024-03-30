def linearSearch(arr1, size, key1):
    for i in range(size):
        if arr1[i] == key1:
            # return 1
            return i



if __name__ == "__main__":

arr = list(map(int, input().split(",")))
key = int(input())

print(linearSearch(arr, len(arr),key))

    # if linearSearch(arr, len(arr), key) == 1:
    #     print("search found")
    # else:
    #     print("search not found")

# Time complexity
# Best Case: Key present in first position(only one iteration is needed)
# Best case time complexity is O(1)
# Worst case: Key present at last position
# Worst case time complexity is O(N)

