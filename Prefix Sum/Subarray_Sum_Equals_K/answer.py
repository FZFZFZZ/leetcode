def subarraySum(nums, k):
    visited = {0: 1}
    count = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in visited:
            count += visited[sum - k]
        if sum in visited:
            visited[sum] += 1
        else:
            visited[sum] = 1
    
    return count