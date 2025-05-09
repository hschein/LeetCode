class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        median_ix = total // 2

        ix1 = ix2 = curr = 0
        for _ in range(median_ix + 1):
            prev = curr
            if ix1 < m and (ix2 >= n or nums2[ix2] > nums1[ix1]):
                curr = nums1[ix1]
                ix1 += 1
            else:
                curr = nums2[ix2]
                ix2 += 1
        
        if total % 2 == 1:
            return curr
        else:
            return (prev + curr) / 2.0
            
