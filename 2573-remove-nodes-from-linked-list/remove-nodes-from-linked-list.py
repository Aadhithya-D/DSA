# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        print(stack)
        res = ListNode(stack[0])
        curr = res
        for i in range(1, len(stack)):
            tmp = ListNode(stack[i])
            curr.next = tmp
            curr = tmp
        return res