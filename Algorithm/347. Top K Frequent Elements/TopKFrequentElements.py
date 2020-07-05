'''
referred to https://zxi.mytechroad.com/blog/hashtable/leetcode-347-top-k-frequent-elements/
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Prioirity queue, max heap
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in counts.keys():
            buckets[counts[num]].append(num)
        ans = []
        for i in range(len(nums), 0, -1):
            ans += buckets[i]
            if len(ans) == k:
                return ans
        return ans
        
 # Time Complexity: O(n)
 # Space Complexity: O(n)
 
 
