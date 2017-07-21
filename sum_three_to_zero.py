#if duplicates ok, e.g. (-1, 1, 0) & (1, -1, 0)
import itertools
def sum_three_to_zero(lst):
    results = []
    for triplet in itertools.combinations(lst, 3):
        if sum(triplet) == 0:
            # print triplet - prints tuple
            results.append(triplet)
    return results




#no duplicates
def sum_3(nums):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums)-1
        while left < right:
            num_sum = nums[i] + nums[left] + nums[right]
            if num_sum == 0:
                results.append((nums[i], nums[left], nums[right]))
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return results