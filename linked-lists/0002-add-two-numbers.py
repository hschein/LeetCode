# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base case:
        if l1 is None and l2 is None:
            if carry != 0:
                return ListNode(carry)
            return None

        # recursive case
        if l1 is not None:
            val1, rest1 = l1.val, l1.next
        else:
            val1, rest1 = 0, None

        if l2 is not None:
            val2, rest2 = l2.val, l2.next
        else:
            val2, rest2 = 0, None

        val = val1 + val2 + carry
        if val >= 10:
            next_carry = 1
            val -= 10
        else:
            next_carry = 0

        return ListNode(val, self.addTwoNumbers(rest1, rest2, next_carry))

# Runtime: 2 ms, beats 92.82% of solutions
# Memory: 12.54 MB, beats 54.54% of solutions
