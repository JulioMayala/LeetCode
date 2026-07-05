class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        newBuy=buy=0
        newSell=sell=0
        for i in range(len(prices)):
            if prices[i]>prices[sell]:
                sell=i
            if prices[i]>prices[newSell]:
                newSell=i
            if prices[i]<prices[newBuy]:
                newBuy=newSell=i
            if (prices[newSell]-prices[newBuy]) > (prices[sell]-prices[buy]):
                sell=newSell
                buy=newBuy
        return prices[sell]-prices[buy]