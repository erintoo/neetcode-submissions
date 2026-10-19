# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while head and hare.next and head.next:
            if tortoise == hare.next:
                return True
            tortoise = tortoise.next
            if hare.next.next:
                hare = hare.next.next
            else:
                return False
        return False