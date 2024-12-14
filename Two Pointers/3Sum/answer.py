def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    n = len(nums)

    for fix in range(n - 2):
        # If the current number is greater than zero, no need to proceed further
        if nums[fix] > 0:
            break

        # Skip duplicate 'fix' elements to avoid duplicate triplets
        if fix > 0 and nums[fix] == nums[fix - 1]:
            continue

        left, right = fix + 1, n - 1
        target = -nums[fix]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                # Append the triplet as it's already sorted
                res.append([nums[fix], nums[left], nums[right]])

                # Move both pointers
                left += 1
                right -= 1

                # Skip duplicates for 'left' pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicates for 'right' pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < target:
                # Need a larger sum; move the left pointer to the right
                left += 1
            else:
                # Need a smaller sum; move the right pointer to the left
                right -= 1

    return res