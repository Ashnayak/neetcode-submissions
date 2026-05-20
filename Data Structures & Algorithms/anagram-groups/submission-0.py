from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for x in strs:
            s = ''.join(sorted(x))
            a[s].append(x)
        return list(a.values())


