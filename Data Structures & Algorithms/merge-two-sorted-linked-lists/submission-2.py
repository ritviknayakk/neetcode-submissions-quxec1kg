# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next      # We need to compare the value at the next node so whe dont do list1.next = list1 we need to move to the next value instead
            else:
                node.next = list2
                list2 = list2.next
            node = node.next        
        node.next = list1 or list2
        return dummy.next

'''# Necessary because otherwise node.next = will keep overwriting the order. 
By doing this node.next will connect to first node, then rewrite to connect to second node. 
Because technically its position would not have changed from where it was. 
By doing node = node.next we change its position'''



