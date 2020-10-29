# Link: https://leetcode.com/problems/valid-parentheses/
# Reference: https://youtu.be/5FUtdNBtbkM

class Solution:
    def isValid(self, s : str) -> bool:
        stack = []
        pairs = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        return len(stack) == 0
