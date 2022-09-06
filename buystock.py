class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpc = float('inf')
        maxpr = 0
        
        for p in prices:
            minpc = min(minpc, p)
            pr = p - minpc
            maxpr = max(maxpr,pr)
            
        return maxpr
