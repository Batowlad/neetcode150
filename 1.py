class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #type: ignore
        hash = {}
        
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        for n in hash:
            if hash[n] > 1:
                return True

        return False
