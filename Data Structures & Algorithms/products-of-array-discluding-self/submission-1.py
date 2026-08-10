class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        prodsWithouti = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prodsWithouti.append(prod//nums[i])
            else:
                prodsWithouti.append(math.prod(nums[:i]+nums[(i+1):]))
        return prodsWithouti
            
             