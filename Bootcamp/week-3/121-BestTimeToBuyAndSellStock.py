class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, profit = prices[0], 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minimum)
            if prices[i] < minimum:
                minimum = prices[i]

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}
        max_profit = 0

        def profit(day):
            nonlocal max_profit
            if day == len(prices) - 1:
                return prices[day]

            if profits.get(day):
                return profits[day]
            next_max = max(prices[day], profit(day + 1))
            max_profit = max(max_profit, next_max - prices[day])
            profits[day] = next_max

            return profits[day]

        profit(0)
        return max_profit
