def subarraySum(nums, k):
    sumArray = [0]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        sumArray.append(sum)
    count = 0
    for i in range(len(sumArray)):
        for j in range(i + 1, len(sumArray)):
            if sumArray[j] - sumArray[i] == k:
                count += 1
    return count

print(subarraySum([1], 0))