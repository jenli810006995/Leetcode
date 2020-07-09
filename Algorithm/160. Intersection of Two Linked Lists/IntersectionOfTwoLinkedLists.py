'''
referred to https://blog.csdn.net/coder_orz/article/details/51615444
'''
# Solution 1:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        :type head1, head1: ListNode
        :rtype: ListNode
        '''
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
                
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
                
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA
    
    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
        
# Solution 2: two pointers iterate the two linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        :type head1, head1: ListNode
        :rtype: ListNode
        '''
        
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p and q and p != q:
            p = p.next
            q = q.next
            
            if p == q:
                return p
            if not p:
                p = headB
            if not q:
                q = headA
                
        return p
   
        
   
