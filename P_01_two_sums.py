def two_sums(nums, target):
    """
    https://leetcode.com/problems/two-sum/
    
    for i in nums:
        get diff of target and current num
        if diff in dict:
            print current num, index of diff in dict
        else
            add num to dict
    """
    nums_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_dict.keys():
            print(i, nums_dict[diff])
            break
        nums_dict[nums[i]] = i


nums1 = [2, 7, 11, 15]
target1 = 9
two_sums(nums1, target1)

nums2 = [3, 2, 4]
target2 = 6
two_sums(nums2, target2)
