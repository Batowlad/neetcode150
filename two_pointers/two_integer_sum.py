class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #type:ignore
        l = 0
        r = len(nums)-1

        for n in nums:
            sum = nums[l] + nums[r]
            
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l+=1
            elif sum > target:
                r-=1