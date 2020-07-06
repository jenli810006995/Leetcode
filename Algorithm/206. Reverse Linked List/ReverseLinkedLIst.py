'''
referred to https://blog.csdn.net/coder_orz/article/details/51306170
'''
# Solution 1: Stack Structure

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        :type head: ListNode
        :rtype:ListNode
        '''
        p = head
        newList = []
        while p:
            newList.insert(0, p.val)
            p = p.next
                             
        p = head
        for v in newList:
            p.val = v
            p = p.next
        return head
      
# Solution 2: Iterative
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        :type head: ListNode
        :rtype:ListNode
        '''
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
        
# Solution 3: Recursive

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(curr):
            if not curr or not curr.next: # base case
                return curr
            reverseRemainder = helper(curr.next)
            curr.next.next = curr # reverse
            curr.next = None # unset next pointer
            return reverseRemainder # return new head
        return helper(head)
             
             
        


