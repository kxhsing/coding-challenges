function findMaxNum(nums) {
    var max = nums[0]
    for (var i = 1; i < nums.length; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }

    return max
}