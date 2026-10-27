class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        num = 0
        dig = len(digits) - 1
        for d in range(len(digits)):
            num += (digits[d]*(10**dig))
            dig -= 1
        num += 1
        while num > 0:
            res.append(num%10)
            num //= 10
        res.reverse()
        return res