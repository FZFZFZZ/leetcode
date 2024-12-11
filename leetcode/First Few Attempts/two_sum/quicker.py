def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        nums[i] = (i, nums[i])
    #nums = list(filter(lambda x: x[1] <= target, nums))   cannot filter like this cuz negative number exists
    nums.sort(key=lambda x: x[1])
    print(nums)
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        tar = target - nums[i][1]
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid][1] == tar:
                return [nums[i][0], nums[mid][0]]
            elif nums[mid][1] < tar:
                left = mid + 1
            else:
                right = mid - 1
nums = [2, 7, 41]
print(twoSum(nums, 9))


