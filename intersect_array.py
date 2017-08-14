def intersection(nums1, nums2):
    """Intersection of 2 arrays"""

    nums1 = set(nums1)
    nums2 = set(nums2)
    result = list(nums1 & nums2)
    
    return result