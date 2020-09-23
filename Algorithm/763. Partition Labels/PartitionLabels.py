## Time: Sep. 22 2020

## A string S of lowercase English letters is given. 
## We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
## and return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        :type S:str
        :rtype: List[int]
        """
        lindex = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, lindex[c])
            if i == j:
                ans.append(j - anchor + 1)
                anchor = j + 1
        return ans
        
## Link: https://leetcode.com/problems/partition-labels/
## Reference: https://blog.csdn.net/fuxuemingzhu/article/details/79265829
        
