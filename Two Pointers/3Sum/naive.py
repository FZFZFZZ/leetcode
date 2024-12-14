def threeSum(nums):
    nums.sort()
    fix = 0
    res = []
    while fix < len(nums) - 2:
       
        l = fix + 1
        r = len(nums) - 1
        while l != r:
            if nums[l] + nums[r] > -nums[fix]:
                r -= 1
            elif nums[l] + nums[r] < -nums[fix]:
                l += 1
            else:
                if [nums[fix], nums[l], nums[r]] not in res:
                    res.append([nums[fix], nums[l], nums[r]])
                l += 1
        fix += 1

    return res
    

Memory = {}
Memory[tuple([1, 2])] = 1
print(Memory)


        
    

