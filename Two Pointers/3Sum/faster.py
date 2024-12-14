def threeSum(nums):
    nums.sort()
    fix = 0
    res = []
    found = {}
    for fix in range(len(nums) - 2):
        if nums[fix] > 0:
            break
       
        l = fix + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > -nums[fix]:
                r -= 1
            elif nums[l] + nums[r] < -nums[fix]:
                l += 1
            else:
                triplet = tuple([nums[fix], nums[l], nums[r]])
                if triplet not in found:
                    res.append([nums[fix], nums[l], nums[r]])
                    found[triplet] = 1
                l += 1
                r -= 1

    return res

print(threeSum([0, 0, 0, 0]))