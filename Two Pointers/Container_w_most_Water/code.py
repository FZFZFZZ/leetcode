def maxArea(height):
    l, r = 0, len(height) - 1
    maxWater = 0
    while (l != r):
        if min(height[r], height[l]) * (r - l) > maxWater:
            maxWater = min(height[r], height[l]) * (r - l)
        else:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
    return maxWater

print(maxArea([1, 3, 2, 5, 25, 24, 5]))