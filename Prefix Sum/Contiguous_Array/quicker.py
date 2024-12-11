def findMaxLength(nums):
    sum = 0
    length = len(nums)
    sumArray = [0]
    for i in range(length):
        sum += -1 if nums[i]==0 else 1
        sumArray.append(sum)
    
    visited = {} 

    for i in range(length):
        if sumArray[i] not in visited:
            visited[sumArray[i]] = i
    
    maxD = 0
    for j in range(length):
        if sumArray[length - j] in visited:
            maxD = max(maxD, length - j - visited[sumArray[length - j]])

    return maxD

print(findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))