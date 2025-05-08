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
        if l1 == None and l2 == None:
            if carry:
                return ListNode(carry)
            return None
        
        # recursive case
        if l1 != None:
            first, next_first = l1.val, l1.next
        else:
            first, next_first = 0, None

        if l2 != None:
            second, next_second = l2.val, l2.next
        else:
            second, next_second = 0, None

        next_val = first + second + carry
        if next_val >= 10:
            next_carry = 1
            next_val -= 10
        else:
            next_carry = 0

        return ListNode(next_val, self.addTwoNumbers(next_first, next_second, next_carry))
