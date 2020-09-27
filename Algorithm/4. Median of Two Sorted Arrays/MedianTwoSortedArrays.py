## Time: 9/26/2020

## Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
## Follow up: The overall run time complexity should be O(log (m+n)).

class Solution():
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        
        if len(nums1) % 2 == 0:
            n = len(nums1) // 2
            return (nums1[n - 1] + nums1[n])/2 # calculating median
            
        else:
            n = (len(nums1) //2) + 1
            return nums1[n - 1]
            
 ## Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
 ## Reference: https://learndataanalysis.org/4-median-of-two-sorted-arrays-leetcode-answers-python/           
            
