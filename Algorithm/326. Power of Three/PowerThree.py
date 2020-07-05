'''
referred to https://blog.csdn.net/coder_orz/article/details/51505792
'''
# recursive:

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
         if n <= 0 :
             return False
         if n == 1:
             return True
         if n % 3 == 0: # modulus
             return self.isPowerOfThree(n/3)
         return False
         
         
         
# follow-up: not using loop or recursive

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
         return n > 0 and 3**19%n == 0
