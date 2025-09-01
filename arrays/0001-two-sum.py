class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {} # dictionary that maps number values to their respective indices
        for ix, num in enumerate(nums):
            if (target - num) in num_to_index:
                return [num_to_index[(target-num)], ix]
            else:
                num_to_index[num] = ix
        
        return []

# Runtime: 0 ms, beats 100% of solutions
# Memory: 13.09 MB, beats 77.48% of solutions
