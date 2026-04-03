# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = dummy = ListNode()

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val//10
            val = val%10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

'''
return dummy.next works because we initially assigned curr and dummy to the same node instance
Then we did curr.next = ListNode(val) whcih made the next point to val which is our first node
Then we did curr = curr.next which keeps moving curr forward
dummny.next gives us first element. We never moved dummy at all 
'''