# Time: July 18 2020

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        '''
        :type t: TreeNode
        :rtype: str
        '''
        if not t:
            return ''
        ans = str(t.val)
        if t.left or t.right: ans += '(' + self.tree2str(t.left) + ')'
        if t.right: ans += '(' + self.tree2str(t.right) + ')'
        return ans
    
    
  # Credit: http://bookshadow.com/weblog/2017/06/04/leetcode-construct-string-from-binary-tree/
