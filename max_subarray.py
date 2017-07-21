def find_max_subarray(nums):
    """Given an array of integers, what is the max sum of any given subarray"""

    best_sum = next_sum = nums[0]

    for num in nums[1:]:
        next_sum = max(num, next_sum += num)
        best_sum = max(best_sum, next_sum)

    return best_sum

