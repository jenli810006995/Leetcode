class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        :type: s: str
        :rtype: str
        """
        s[:] = [s[len(s) - i - 1] for i in range(len(s))]
        
        
