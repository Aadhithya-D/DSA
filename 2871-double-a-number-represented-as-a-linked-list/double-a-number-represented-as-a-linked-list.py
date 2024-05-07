# Definition for singly-linked list.
import sys
sys.set_int_max_str_digits(0)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        current = head
        while current:
            n = n*10 + current.val
            current = current.next
        n = n*2
        n = str(n)
        res = ListNode(n[0])
        curr = res
        for i in range(1, len(n)):
            t = ListNode(n[i])
            curr.next = t
            curr = t
        return res
        