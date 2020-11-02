Time: 10/13/2020

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

 
```
Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0

```

Solution:

```
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        d = dict()
        div, mod = self.divmod(numerator, denominator)
        if mod == 0:
            return str(div)
        ans = "-" if ((numerator > 0)^(denominator > 0)) else ""
        div, mod, denominator = abs(div), abs(mod), abs(denominator)
        ans += str(div) + "."
        d[mod] = len(ans)
        while mod:
            mod *= 10
            div, mod = self.divmod(mod, denominator)
            ans += str(div)
            if mod in d:
                index = d[mod]
                ans = ans[:index] + "(" + ans[index:] + ")"
                break
            else:
                d[mod] = len(ans)
        return ans
        
    def divmod(self, a, b):
        q = int(a/b)
        r = a - b*q
        return (q, r)
```
[Link](https://leetcode.com/problems/fraction-to-recurring-decimal/)

[Reference](https://blog.csdn.net/fuxuemingzhu/article/details/82533218)


