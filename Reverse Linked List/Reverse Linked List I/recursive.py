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
        def helper(head, res):
            if head != None:
                return helper(head.next, ListNode(head.val, res))
            else:
                return res
        return helper(head, None)