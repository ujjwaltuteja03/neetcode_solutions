# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        
        sublistHead = prev.next
        sublistTail = sublistHead
        for _ in range(right-left):
            sublistTail = sublistTail.next
        
        next_node = sublistTail.next
        sublistTail.next = None
        reversed_sublist = self.reverseList(sublistHead)
        prev.next = reversed_sublist
        sublistHead.next = next_node
        return dummy.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead