def find_largest_smaller_than(nums, xnumber):
    """Find the largest number in a list(nums) that is smaller than the target (xnumber)"""
        
    if nums[0] > xnumber:
        return False

    if nums[-1] < xnumber:
        return len(nums) - 1

    for i, num in enumerate(nums):
        if num > xnumber:
            return i-1


