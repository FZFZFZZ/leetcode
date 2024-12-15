class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        # Compute the initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window from index k to the end
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / float(k)