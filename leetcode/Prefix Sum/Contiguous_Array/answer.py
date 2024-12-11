def findMaxLength(nums):
    sum = 0
    visited = {0: 0} 
    maxD = 0

    for i, num in enumerate(nums):
        sum += 2 * nums[i] - 1
        if sum not in visited:
            visited[sum] = i + 1
        else: 
            maxD = max(maxD, i + 1 - visited[sum])

    return maxD


print(findMaxLength([0, 1]))