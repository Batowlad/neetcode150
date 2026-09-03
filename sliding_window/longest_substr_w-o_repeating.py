class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #type: ignore
        substring = ""
        max_len = 0
        start, end = 0, 1
        for x in s:
            print(f"start:{substring}:end")
            if x in substring:
                if max_len < len(substring):
                    max_len = len(substring)
                start = end
                substring = ""
            substring+=x
            end+=1

        
        return max_len