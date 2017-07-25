def find_target_index(nums, target):
    """Given a list of sorted numbers, find what the index of the target is if
    if it's present in the list, or where it would be if it isn't"""

    if target > nums[len(nums)-1]:
        return len(nums)

    if target < nums[0]:
        return 0

    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)/2

        if target < nums[mid]:
            r = mid - 1
            if r >= 0:
                if target > nums[r]:
                    return r+1
            else:
                return 0

        elif target > nums[mid]:
            l = mid + 1
            if l < len(nums):
                if target < nums[l]:
                    return l
            else:
                return len(nums)
        else:
            return mid


