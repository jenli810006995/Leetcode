class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letter_at_index = ""
        final_string = ""
        
        if len(strs) == 0:
            return final_string
            
        for index_in_string in range(0, len(strs[0])):
            for index, string in enumerate(strs):
                try:
                    if index == 0:
                        letter_at_index += string[index_in_string]
                    elif string[index_in_string] != letter_at_index:
                        return final_string
                    else:
                        pass
                except IndexError:
                    return final_string
                    
            final_string += letter_at_index
            letter_at_index = ""
        return final_string
        
        
  ## Link: https://leetcode.com/problems/longest-common-prefix/
  ## Reference: https://dfrieds.com/python/longest-common-prefix-python.html
       
       
