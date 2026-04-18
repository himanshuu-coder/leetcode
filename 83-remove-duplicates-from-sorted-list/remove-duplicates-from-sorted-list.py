# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single node list
        if not head:
            return head
        
        current = head
        
        # Traverse until the second to last node
        while current and current.next:
            if current.val == current.next.val:
                # Skip the next node because it's a duplicate
                current.next = current.next.next
            else:
                # Only move forward if no duplicate was found at the current position
                current = current.next
                
        return head