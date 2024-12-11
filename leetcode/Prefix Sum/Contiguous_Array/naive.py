def findMaxLength(nums):
    sum = 0
    length = len(nums)
    sumArray = []
    for i in range(length):
        sum += nums[i]
        sumArray.append(sum)
    
    max = 0
    for i in range(length):
        for j in range(i, length):
            prev = 0 if i == 0 else sumArray[i - 1]
            if ((sumArray[j] - prev) * 2 == j - i + 1) and j - i + 1 > max:
                max = j - i + 1
    
    return max

