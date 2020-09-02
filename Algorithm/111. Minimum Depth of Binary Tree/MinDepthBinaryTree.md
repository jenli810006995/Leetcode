Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
```

* Solution in CPP:
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        
        if(root == NULL){
            return 0;
        }
        
        /* reached to the left */
        
        if (root-> left == NULL && root-> right != NULL){
            return minDepth(root-> right) + 1;
        }
        
        /* reached to the right*/
        
        else if (root-> left != NULL && root-> right == NULL){
            return minDepth(root-> left) + 1;
        }
        
        /* not the above cases, choose the min of the both*/
        
        else{
            int left = minDepth(root-> left) + 1;
            int right = minDepth(root-> right) + 1;
            return (left < right? left:right);
            
        }
        
    }
};
```
* [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
* [Reference](https://gist.github.com/soundsilence/4646951)
