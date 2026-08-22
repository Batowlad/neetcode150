class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #type: ignore
        hash = {}

        for i, n in enumerate(nums):
            print((i, n))
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i