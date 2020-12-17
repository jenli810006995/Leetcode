* Time: Aug 15 2020

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

```
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

* Logic: Firstly, create a empty list, and then loop from 1 to n+1(as in Python 3, the n+1 is not included).
Secondly, use modulus in the if statements. First check if the number is the multiplier of 15, and then 5, and then 3.
As the multiplier of 5 or 3 can also be the multiplier of 15. Lastly, the output is a list of strings.

* Solution:
```
class Solution:
    def fizzBuzz(self, n: int) -> List[str]: 
        ans = []
        for x in range(1, n+1):
            n = str(x)
            if x % 15 == 0:
                n = "FizzBuzz"
            elif x % 5 == 0:
                n = "Buzz"
            elif x % 3 == 0:
                n = "Fizz"
            ans.append(n)
        return ans
```

* [Link](https://leetcode.com/problems/fizz-buzz/)
