# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        see, cur=set(), head
        while cur:
            if cur in see:
                return True
            see.add(cur)
            cur=cur.next
        return False