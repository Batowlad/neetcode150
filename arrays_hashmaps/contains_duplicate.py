class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #type: ignore
        hash = {}
        
        for n in nums:
            if n in hash:
                return True
            else:
                hash[n] = 1

        return False
