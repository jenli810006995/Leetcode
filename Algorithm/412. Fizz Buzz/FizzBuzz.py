'''
referred to https://blog.csdn.net/NXHYD/article/details/72314080
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
     
         for x in range(1, n + 1):
            n = str(x)
            if x % 15 == 0:
                n ='FizzBuzz'
            elif x % 3 == 0:
                n ='Fizz'
            elif x % 5 == 0:
                n = 'Buzz'
            ans.append(n)
                
        return ans
        
# Time Complexity: O(n)
# Space Complexity: O(1)


    
