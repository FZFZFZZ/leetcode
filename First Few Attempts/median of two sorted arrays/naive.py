def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def median(arr):
        if len(arr) % 2 == 1:
            return arr[len(arr) // 2]
        else:
            return float(arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        
    i = 0
    j = 0
    res = []
    if len(nums1) == 0:
        return median(nums2)
    elif len(nums2) == 0:
        return median(nums1)

    while (i < len(nums1) and j < len(nums2)):
        if (nums1[i] > nums2[j]):
            res.append(nums2[j])
            j += 1
        else:
            res.append(nums1[i])
            i += 1
    if i == len(nums1):
        res += nums2[j:]
    else:
        res += nums1[i:]
    return median(res)

print(findMedianSortedArrays([1], [3, 4, 5]))