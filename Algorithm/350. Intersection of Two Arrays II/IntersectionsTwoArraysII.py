'''
referred to http://bookshadow.com/weblog/2016/05/21/leetcode-intersection-of-two-arrays-ii/
'''

# One Option:

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1 = p2 = 0
        ans = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ans += nums1[p1],
                p1 += 1
                p2 += 1
        return ans
        
       
# Two Option: Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c = collections.Counter(nums1)
        ans = []
        for x in nums2:
            if c[x] > 0:
                ans += x,
                c[x] -=1
                
        return ans
    
   
