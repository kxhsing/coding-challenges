

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i, num in enumerate(nums):
        m = target - num
        if m in dic:
            return [dic[m], i]
        else:
            dic[num] = i


#eg, [3, 2, 4] target=6 --> answer = [1, 2]
# for i=3, num=3 --> m = 6 - 3 = 3. is 3 in dic? no, so add dic[3] = 0
# for i=1, num=2 --> m = 6 - 2 = 4. is 4 in dic? no, so add dic[2] = 1
# for i=2, num=4 --> m = 6 - 4 = 2. is 2 in dic? YES! so return [dic[2]==1, 2]


