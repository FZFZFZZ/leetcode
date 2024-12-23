class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp

        prev.next.next = curr
        prev.next = next_node
        
        return dummy.next
    

# This is the answer.