class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        median_ix = total_length // 2

        if not nums1:
            merged_arr = nums2
        elif not nums2:
            merged_arr = nums1
        elif nums1[-1] <= nums2[0]:
            merged_arr = nums1 + nums2
        elif nums2[-1] <= nums1[0]:
            merged_arr = nums2 + nums1
        else:
            merged_arr = []
            while len(merged_arr) <= median_ix:
                if not (nums1 and nums2):
                    merged_arr = merged_arr + nums1 + nums2
                elif nums1[0] <= nums2[0]:
                    merged_arr.append(nums1.pop(0))
                else:
                    merged_arr.append(nums2.pop(0))

        # if length is even, median is average of middle two nums
        if total_length % 2 == 0:
            return (merged_arr[median_ix-1] + merged_arr[median_ix]) / 2.0
        # otherwise it is just middle number
        else:
            return merged_arr[median_ix]
