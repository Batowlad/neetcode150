# MY VERY OWN VERY ORIGINAL SOLUTION THAT BEATS 92% MEMORY, but is shit otherwise
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: #type: ignore
        hash = {}
        top = []

        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        
        value_list = list(hash.values())
        key_list = list(hash.keys())

        for f in range(k):
            top.append(key_list[value_list.index(max(value_list))])
            key_list.remove(key_list[value_list.index(max(value_list))])
            value_list.remove(max(value_list))
            
        
        return top
#################################################################################

