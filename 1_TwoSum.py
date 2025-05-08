class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)
        for num in set_nums:
            if (target - num) != num and (target - num) in set_nums:
                result_vals = (num, target-num)
                return [nums.index(num), nums.index(target-num)]

        # if it gets here, the answer is a duplicate
        val = target // 2
        result = []
        for ix, num in enumerate(nums):
            if num == val:
                result.append(ix)
                if len(result) == 2:
                    return result
