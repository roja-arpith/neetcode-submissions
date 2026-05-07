class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_Profit = 0
        price = prices[0]

        for i in range(len(prices)):
            price = min(price, prices[i])
            max_Profit = max(max_Profit, prices[i] - price)
        
        return max_Profit