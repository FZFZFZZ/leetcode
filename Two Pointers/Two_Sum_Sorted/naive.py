def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l != r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
    
    return None

# inline logic is faster than assignment
# this solution is optimal enough
