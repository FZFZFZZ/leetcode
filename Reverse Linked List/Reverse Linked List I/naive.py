
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = None

        while head != None:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node
    
# This is the official answer that needs to be memorised.

        
