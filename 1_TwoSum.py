class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for ix, num in enumerate(nums):
            if (target - num) in num_to_index:
                return [num_to_index[(target-num)], ix]
            else:
                num_to_index[num] = ix
        
        return []
