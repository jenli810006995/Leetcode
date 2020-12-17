class Solution:
    res = None
    def findmax(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            max_l = self.findmax(root.left)
            max_r = self.findmax(root.right)
            max_s = max(max(max_l, max_r)+root.val, root.val)
            max_top = max(max(max_s, max_l+max_r+root.val), root.val)
            if self.res == None:
                self.res = max_top
            else:
                self.res = max(self.res, max_top)
            return max_s
    def maxPathSum(self, root):
        self.findmax(root)
        return self.res    
        
        
 ## Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
 ## Reference: http://yucoding.blogspot.com/2012/12/leetcode-question-13-binary-tree.html
