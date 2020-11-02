'''
referred to http://bookshadow.com/weblog/2015/12/31/leetcode-wiggle-sort-ii/
run in Python instead of Python 3
'''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # sort the original array
        # pop the tail to the subscription of the even positions
        # pop the tail to the subscription of the odd position
        
        size = len(nums)
        snums = sorted(nums)
        
        for i in range(1, size, 2) + range(0, size, 2): # range(start, stop, step)
            nums[i] = snums.pop()
            
 # Time: O(nlongn)
 # Spece: O(n)
 
 # Solution 2: O(n) and O(1)
 # Use C++
 
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        
        // Find a median
        
        auto midptr = nums.begin() + n/2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;
        
        // Index-rewriting: greater than mid in the smaller idx, and vise versa
        #define A(i) nums[(1 + 2*(i)) % (n|1)]
        
        // 3-way-partition-to-wiggly in O(n) time with O(1) space
        int i = 0, j = 0, k = n-1;
        while (j <= k){
            if (A(j) > mid)
                swap(A(i++), A(j++));
            else if (A(j) < mid)
                swap(A(j), A(k--));
            else
                j++;
        }
        
    }
};
 
 
