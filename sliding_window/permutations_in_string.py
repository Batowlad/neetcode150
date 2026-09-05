class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: #type:ignore
        s1 = list(s1)
        s2 = list(s2)

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)-1

        s1_hash = {}
        for char in s1:
            if char not in s1_hash:
                s1_hash[char] = 1
            else:
                s1_hash[char] += 1
        while r<(len(s2)+1):
            s2_hash = {}
            for char in s2[l:r+1]:
                if char not in s2_hash:
                    s2_hash[char] = 1
                else: 
                    s2_hash[char] += 1

            if s2_hash == s1_hash:
                return True
            
            l+=1
            r+=1

        return False