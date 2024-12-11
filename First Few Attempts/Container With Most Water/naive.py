def maxArea(height):
    maxWater = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            water = (j - i) * min(height[j], height[i])
            if water > maxWater:
                maxWater = water
    return maxWater

print(maxArea([1,8,6,2,5,4,8,3,7]))