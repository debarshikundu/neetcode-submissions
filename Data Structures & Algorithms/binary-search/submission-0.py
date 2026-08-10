class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        low = 0
        high = len(nums)-1

        mid = math.floor((low + high)/2)
        while low <= high:
            mid = math.floor((low + high)/2)
            if nums[mid] == target:
                index = mid
                return index
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return index
            
