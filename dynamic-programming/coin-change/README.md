# Coin Change

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/coin-change/

## Problem

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

## Approach

Bottom-up one-dimensional dynamic programming

## Explanation

For every subtotal, try appending each coin to the best solution for subtotal minus that coin.

## Complexity

- Time: O(amount * numberOfCoins)
- Space: O(amount)

## Alternatives

Breadth-first search over reachable totals, or memoized recursion.

## Common mistakes

Using a zero default for unreachable totals, which makes impossible states look optimal.

## Learning notes

Choose an impossible sentinel and build every amount from smaller solved amounts.

## Solution

```python
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

```
