'''
referred to https://blog.csdn.net/coder_orz/article/details/51516558
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1:

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # create a dict
        
        '''
        :type head: ListNode
        :rtype: bool
        
        '''
        map = {}
        while head:
            if id(head) in map:
                return True
            else:
                map[id(head)] = True
            head = head.next
        return False
 
# Time Complexity: O(n), Space Complexity: O(n)
    
# Solution 2: Slow and Fast Pointers
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # slow and fast pointers
        
        '''
        :type head: ListNode
        :rtype: bool
        
        '''
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# Time Complexity: O(n)
# Space Complexity: O(1)


    
    
