'''
referred to https://blog.csdn.net/coder_orz/article/details/51306985
'''

# Solution 1: Time Complexity: O(n), Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
            
        length = len(temp_list)
        
        for i in range(length//2):
            if temp_list[i] != temp_list[length - i - 1]:
                return False
        return True
        
        
# Solution 2: Time: O(n), Space: O(n/2)
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        new_list = []
        
        slow = fast = head
        
        while fast and fast.next:
            new_list.insert(0, slow.val)
            
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        for val in new_list:
            if val != slow.val:
                return False
            slow = slow.next
            
        return True
        
        
# Solution 3: Time: O(n), Space: O(1)
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        new_list = []
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next # slow points to the latter half
        slow = self.reserveList(slow)
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
    def reserveList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
                
