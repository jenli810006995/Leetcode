* Time: Aug 17 2020

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

```
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
``` 

Note: You may assume the string contains only lowercase English letters.

* Logic:
1. Create an empty dictionary
2. Loop through the string, for each c in s, check whether seen before by using the command "if c in letters" then letters[c]+1 else 1, 
which meant that the character has only seen once
3. for i in range(len(s)), here i means the index of the string s, if letters[s[i]] == 1, which means the s[i] is the unique character,
return i; else return -1

* Solution:

```
class Solution:
    def firstUniqChar(self, s:str) -> int:
        letters = {} # create an empty dictionary
        
        for c in s:
            letters[c] = letters[c]+1 if c in letters else 1 #if seen before then plus 1 else put 1 means the first seen
            
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1
```

* [Link](https://leetcode.com/problems/first-unique-character-in-a-string/submissions/)

