# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # Initialize the index counters to use for arrA, arrB and merged_arr
    i = 0
    j = 0
    k = 0

    # Whilst the end of both arrays hasn't been reached, compare the two indexes of each array and add the smallest to merged_arr
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    # Once the end of one array has been reached, add the remainder of the other array to merged_arr.
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    # print(merged_arr)
    return merged_arr


# print(merge([1, 5, 8, 4, 2], [9, 6, 0, 3, 7))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    middle = len(arr) // 2
    lhs = arr[:middle]
    rhs = arr[middle:]
    if len(arr) > 1:
        # print(f"lhs: {lhs}")
        # print(f"rhs: {rhs}")
        lhs_arr = merge_sort(lhs)
        rhs_arr = merge_sort(rhs)

        arr = merge(lhs_arr, rhs_arr)

    return arr


# print(merge_sort([1, 5, 7, 8, 2, 4, 6, 9]))
# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
