class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        while n != 1 and not (n in res):
            res.append(n)
            n = self.sHappy(n)
        return n == 1

    def sHappy(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += ((n % 10) ** 2)
            n //= 10
        return sum
