from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        answer = True
        
        ran_list = list(ransomNote)
        mag_list = list(magazine)
        
        ran_cnt = dict(Counter(ran_list))
        mag_cnt = dict(Counter(mag_list))
        
        ran_keys = ran_cnt.keys()
        mag_keys = mag_cnt.keys()
        
        for r_key in ran_keys:
            if r_key not in mag_keys:
                answer = False
                break
                
            # mag_cnt and ran_cnt are two dictionary structure
            check = mag_cnt[r_key] - ran_cnt[r_key]
            if check < 0:
                answer = False
                break
                
        return answer
        
   ## Link: https://leetcode.com/problems/ransom-note/
   ## Reference: https://somjang.tistory.com/entry/leetCode-383-Ransom-Note-Python
