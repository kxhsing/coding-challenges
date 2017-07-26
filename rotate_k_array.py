def rotate(nums, k):
    """Rotate nums in list by k positions to the right"""

    k = k % len(nums)

    nums[:] = nums[-k:] + nums[:-k]