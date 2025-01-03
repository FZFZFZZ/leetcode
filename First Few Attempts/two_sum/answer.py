def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
        return []  # No solution found

nums = [2, 7, 41]
print(twoSum(nums, 9))