# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive: T:O(n), M: O(n)
        if not head:
            return None
            
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
          
        
# Link: https://leetcode.com/problems/reverse-linked-list/
