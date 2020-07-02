'''
referred to https://zxi.mytechroad.com/blog/bit/leetcode-1404-number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
'''

class Solution:
    def numSteps(self, s: str) -> int:
        # -> "hint"
        
        ans, carry = 0, 0
        
        for i in range(1, len(s)):
            if ord(s[-i]) - ord('0') + carry == 1:
                ans += 2
                carry = 1
            else:
                ans += 1
        return ans + carry
        
      
