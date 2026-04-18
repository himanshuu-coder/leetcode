class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize costs to infinity and profits to 0
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for price in prices:
            # 1. First Buy: Minimize the money spent
            buy1 = min(buy1, price)
            
            # 2. First Sell: Maximize profit (Current Price - First Buy Cost)
            sell1 = max(sell1, price - buy1)
            
            # 3. Second Buy: Minimize effective cost (Current Price - Profit from Sell 1)
            # This is like saying "I'm using my first profit to help pay for the second stock"
            buy2 = min(buy2, price - sell1)
            
            # 4. Second Sell: Maximize final profit (Current Price - Effective Buy 2 Cost)
            sell2 = max(sell2, price - buy2)
            
        return sell2