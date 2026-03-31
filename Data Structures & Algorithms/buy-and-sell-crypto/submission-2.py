class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        amount=0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                amount=max(amount, prices[r]-prices[l])
            r+=1

        return amount