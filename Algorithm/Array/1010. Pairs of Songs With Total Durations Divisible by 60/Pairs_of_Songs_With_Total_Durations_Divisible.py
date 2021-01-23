class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60 == 0 && b%60 == 0
                ret += remainders[0]
                
            else: # check if a%60 + b%60 == 60
                ret += remainders[60 - t%60]
            remainders[t % 60] += 1
        return ret
          
# T: O(N)
# M: O(1)
# Link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

        
