class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sety = set(nums)
        maxy = 0

        for n in nums:
            if (n-1) not in sety:
                length = 0
                while (n+length) in sety:
                    length += 1
                maxy = max(maxy, length)
        return maxy

        