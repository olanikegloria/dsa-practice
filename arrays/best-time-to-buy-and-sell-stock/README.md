# Best Time to Buy and Sell Stock

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Approach

Single pass min tracking

## Explanation

Track min so far; maximize price - min.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Kadane on differences.

## Common mistakes

Allowing sell before buy.

## Learning notes

Running extrema unlock many array profits.

## Solution

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best

```
