'''
referred to http://bookshadow.com/weblog/2016/01/16/leetcode-odd-even-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        if head is None: return head
        odd = oddHead = head
        even = evenHead = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead
        
        
