class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoListsUsingForLoop(l1, l2):
    dummy = ListNode(0)
    ans = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    dummy.next = l1 if l1 is not None else l2
    return ans.next

def mergeTwoListsUsingRecursion(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoListsUsingRecursion(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsUsingRecursion(l1, l2.next)
        return l2
    