# Dutch national flag problem


def simple_counting_1(arr):
    """
    Count the number of 0, 1 2.
    Create new array and put the required number of elements.
    """
    num_counts = {}
    for i in arr:
        if i in num_counts:
            num_counts[i] += 1
        else:
            num_counts[i] = 1

    result_arr = []
    for j in sorted(num_counts.keys()):
        for _ in range(num_counts[j]):
            result_arr.append(j)

    print(result_arr)


def simple_counting_2(arr):
    """
    Traverse arr and put elements in new array in one pass
    """
    result_arr = []
    index_of_one = 0
    for i in arr:
        if i == 2:  # push to end
            result_arr.append(i)
        elif i == 1:  # put in middle and increment index
            result_arr.insert(index_of_one, i)
            index_of_one += 1
        elif i == 0:  # insert at beginning and increment index
            result_arr.insert(0, i)
            index_of_one += 1

    print(result_arr)


def sort_0_1_2(arr):
    """
    Traverse aray once. So in-place swapping.
    """
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid < high:
        if arr[mid] == 0:  # swap with low. low++, mid++
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:  # mid++
            mid += 1
        elif arr[mid] == 2:  # swap with high. high--
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    print(arr)


arr1 = [0, 1, 2, 0, 1, 2]
arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# simple_counting_1(arr1)
# simple_counting_1(arr2)
#
# simple_counting_2(arr1)
# simple_counting_2(arr2)

sort_0_1_2(arr1)
sort_0_1_2(arr2)

