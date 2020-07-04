'''
referred to http://bookshadow.com/weblog/2016/09/04/leetcode-longest-substring-with-at-least-k-repeating-characters/
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        :type s: str
        :type k: int
        :rtype: int
        '''
        
        cnt = collections.Counter(s)
        filters = [x for x in cnt if cnt[x] < k ]
        
        if not filters:
            return len(s)
        
        tokens = re.split('|'.join(filters), s)
        return max(self.longestSubstring(t,k) for t in tokens)
    
