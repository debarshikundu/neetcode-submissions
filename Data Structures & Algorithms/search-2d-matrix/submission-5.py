class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowR = 0
        highR = len(matrix)-1
        midR = 0

        lowC = 0
        highC = len(matrix[0])-1
        midC = 0

        while lowR<=highR:
            midR = (lowR+highR)//2
            if target in matrix[midR]:
                break
            elif target > max(matrix[midR]):
                lowR = midR + 1
            else: 
                highR = midR - 1
        while lowC<=highC:
            midC = (lowC+highC)//2
            if target == matrix[midR][midC]:
                return True
            elif target > matrix[midR][midC]:
                lowC = midC + 1
            else:
                highC = midC - 1
        return False
