from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        unreachable = amount + 1
        dp = [0] + [unreachable] * amount
        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], dp[total - coin] + 1)
        return -1 if dp[amount] == unreachable else dp[amount]
