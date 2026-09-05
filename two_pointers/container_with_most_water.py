class Solution:
    def maxArea(self, h: List[int]) -> int: #type:ignore
        l, r = 0, len(h)-1
        max_area = min(h[l], h[r]) * (r-l)
        for x in h:
            if h[l] < h[r] or h[l]==h[r] and l<r:
                l+=1
            elif h[r] < h[l]:
                r-=1
            area = min(h[l], h[r]) * (r-l)
            max_area = max(max_area, area)

        return max_area