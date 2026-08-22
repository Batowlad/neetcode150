#playing around - mostly figuring out the stuff for the solution

from collections import defaultdict
x = defaultdict(list)
x[1].append("soldia")
x[1].append("boy")
print(x)

d = defaultdict(list)
l = [0]*26
print(l)
l[1] +=1
print(l)
d[tuple(l)].append("suka")
print(d)
#################################################################

# An actual solution through hash maps - had to look into it but I understand how it works
class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:#type:ignore
        d = defaultdict(list)
        
        for s in strings:
            letter_count = [0]*26
            for c in s:
                letter_count[ord(c)-ord("a")] += 1
            d[tuple(letter_count)].append(s)
        return list(d.values())
###########################################################################################

# Solution using sort
class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]: #type:ignore
        d = defaultdict(list)
        
        for s in strings:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())