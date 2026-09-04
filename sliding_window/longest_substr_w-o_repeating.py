class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        max_len = 0
        start = 0
        for end in range(len(s)):
            if s[end] in substring:
                start = max(substring[s[end]]+1, start)
            substring[s[end]] = end 
            max_len = max(max_len, end-start+1)
        return max_len