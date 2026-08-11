class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1=1
        index2=len(numbers)

        while (index1)<(index2):
            s = (numbers[(index1-1)]+numbers[(index2-1)])
            if s==target:
                return [index1, index2]
            elif s < target:
                index1 += 1
            elif s > target:
                index2 -= 1
        return []