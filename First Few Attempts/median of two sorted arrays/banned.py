class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        res = nums1 + nums2
        res.sort()
        n = len(res)
        mid = n // 2
        if n % 2 == 1:
            return res[mid]
        else:
            return float(res[mid - 1] + res[mid]) / 2


'''
Why is it Fast in Practice?
Python's Built-In Sorting (Timsort) is Highly Optimized:
The sort() function in Python uses Timsort, which is a hybrid sorting algorithm derived from merge sort and insertion sort.
Timsort is adaptive: It is extremely fast for data that is already partially sorted, which is often the case when merging two sorted arrays (nums1 and nums2).
Even for random data, the sorting process performs better than many other general-purpose sorting algorithms.
'''