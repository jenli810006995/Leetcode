'''
referred to https://youtu.be/wflOklo8wNU
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ## recursive
        
        count = 0
        
        def go(node, v):
            nonlocal count
            if node is None:
                return
            
            if node.val >= v:
                count +=1
            
            go(node.left, max(node.val, v))
            go(node.right, max(node.val, v))

        go(root, -(1<<30))
        
        return count
    
   
