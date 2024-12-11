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
    count = (len(nums1) + len(nums2)) // 2 + 1

    while (i + j < count):
        if i > len(nums1) - 1:
            res.append(nums2[j])
            j += 1
        elif j > len(nums2) - 1:
            res.append(nums1[i])
            i += 1   
        elif nums1[i] > nums2[j]:
            res.append(nums2[j])
            j += 1
        else:
            res.append(nums1[i])
            i += 1
    return res[-1] if (len(nums1) + len(nums2)) % 2 == 1 else float(res[-1] + res[-2]) / 2

print(findMedianSortedArrays([-1, 3, 5], [0, 1, 2]))