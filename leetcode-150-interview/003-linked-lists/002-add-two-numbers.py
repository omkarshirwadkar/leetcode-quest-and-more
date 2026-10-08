class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbersSmallerSolution(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        columnSum = val1 + val2 + carry
        carry = (columnSum // 10)
        curr.next = ListNode(columnSum % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def addTwoNumbersLongSolution(l1, l2):
    l1h = l1
    l2h = l2
    carry = 0
    res = ListNode(0)
    ans = res
    while l1h and l2h:
        currSum = carry + l1h.val + l2h.val
        carry = currSum // 10
        curr = ListNode(currSum % 10)
        res.next = curr
        res = res.next
        l1h = l1h.next
        l2h = l2h.next
    while l1h:
        currSum = carry + l1h.val
        carry = currSum // 10
        curr = ListNode(currSum % 10)
        res.next = curr
        res = res.next
        l1h = l1h.next
    while l2h:
        currSum = carry + l2h.val
        carry = currSum // 10
        curr = ListNode(currSum % 10)
        res.next = curr
        res = res.next
        l2h = l2h.next
    if carry:
        curr = ListNode(carry)
        res.next = curr
    return ans.next