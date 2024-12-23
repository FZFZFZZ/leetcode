# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = ListNode(0)
        prev.next = head
        if prev.next and prev.next.next:
            start = head.next
        else:
            return head
            
        while prev.next and prev.next.next:
            temp1 = prev.next.next.next
            temp2 = prev.next.next

            temp2.next = prev.next
            prev.next.next = temp1
            prev.next = temp2
            prev = prev.next.next
        
        return start
            

# This answer is good enough