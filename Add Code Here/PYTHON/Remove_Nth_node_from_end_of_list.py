# Leetcode Problem: 19
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        slow = head
        fast = head
        previous = head
      
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            previous = slow
            slow = slow.next
        if slow == head:
            head = slow.next   
        if previous:
            previous.next = slow.next
        
        return head
