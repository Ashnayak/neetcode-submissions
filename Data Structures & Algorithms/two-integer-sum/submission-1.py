class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            for j in range(i+1,len(nums)):
                if b == nums[j]:
                    return[i,j]