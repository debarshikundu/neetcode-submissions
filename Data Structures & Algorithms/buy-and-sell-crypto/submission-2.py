class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(1,len(prices)):
            profits.append(prices[i]-min(prices[0:i]))
        if profits == [] or max(profits) < 0:
            return 0
        return max(profits)



            
