class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node

def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    def end(carry, l):
        if l == None:
            if carry == 1:
                return ListNode(1, None)
            else:
                return None
        else:
            value = (l.val + carry) % 10
            carry = (l.val + carry) // 10
            return ListNode(value, end(carry, l.next))
        
    def helper(carry, l1, l2):
        if l1 == None:
            return end(carry, l2)
        elif l2 == None:
            return end(carry, l1)
        else:
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            return ListNode(value, helper(carry, l1.next, l2.next))
    return helper(0, l1, l2)
