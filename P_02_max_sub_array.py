def max_subarray(arr):
    """
    https://leetcode.com/problems/maximum-subarray/
    linear solution - sliding window method
    """
    max_sub_arr_sum = arr[0]
    current_sum = 0
    for i in arr:
        if current_sum < 0:
            current_sum = 0
        current_sum = current_sum + i
        max_sub_arr_sum = max(max_sub_arr_sum, current_sum)

    print(max_sub_arr_sum)


arr1 = [10, 20, 30, 40, 50, 60, 70, 80]
max_subarray(arr1)

arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray(arr2)
