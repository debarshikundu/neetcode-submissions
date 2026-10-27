class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in range(len(nums)):
            if nums[n] not in nums[:n] and nums[n] not in nums[n+1:]:
                return nums[n]
        return