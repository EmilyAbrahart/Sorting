# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


print(selection_sort([2, 5, 7, 3, 8, 1, 4]))  # [1, 2, 3, 4, 5, 7, 8]

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([2, 5, 7, 3, 8, 1, 4]))  # [1, 2, 3, 4, 5, 7, 8]


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) < 2:
        return arr
    else:
        for x in arr:
            if x < 0:
                return 'Error, negative numbers not allowed in Count Sort'
        if maximum == -1:
            maximum = max(arr)
        m = maximum + 1
        count = [0] * m     # Initialize count array with 0s
        for a in arr:
            # Count the occurences of each value by adding one to the corresponding value in the count array
            count[a] += 1
        i = 0
        for a in range(m):
            for c in range(count[a]):
                arr[i] = a
                i += 1
        return arr

# print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

