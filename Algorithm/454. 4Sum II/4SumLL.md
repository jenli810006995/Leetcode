* Time: Aug 15 2020

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2
```
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

* Logic: Firstly, create a dictionary. And then, traverses A and B, stores and value and count and A+B.
Secondly, traverses C and D. If -c-d in the dictionary, it indicates that a pair has been found. And the count of it is accumulated.
Notice: Solution is upper class S. fourSumCount is lower class f

* Solution:
```
class Solution:
    def fourSumCount(self, A:List[int], B:List[int], C:List[int], D:List[int]) -> int:
        mp = dict() # create a dictionary
        for a in A:
            for b in B:
                mp[a+b] = mp.get(a+b,0) +1
                
        count = 0
        for c in C:
            for d in D:
                if -c-d in mp:
                    count += mp[-(c+d)]
                    
        return count
```

* [Link](https://leetcode.com/problems/4sum-ii/submissions/)
* [Credit](https://www.programmersought.com/article/3096670707/)

