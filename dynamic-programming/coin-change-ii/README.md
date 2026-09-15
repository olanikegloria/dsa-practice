# Coin Change II

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/coin-change-ii/

## Problem

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the number of combinations that make up that amount.

## Approach

DP coin outer loop

## Explanation

Unbounded knapsack counting combinations; iterate coins outer.

## Complexity

- Time: O(amount * coins)
- Space: O(amount)

## Alternatives

Recursion with memo.

## Common mistakes

Permutation vs combination order in loops.

## Learning notes

Coin outer loop counts combinations not permutations.

## Solution

```python
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]

```
