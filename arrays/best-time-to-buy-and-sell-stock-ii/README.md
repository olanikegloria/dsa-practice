# Best Time to Buy and Sell Stock II

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## Problem

You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. Return the maximum profit you can achieve from this transaction.

## Approach

Greedy accumulate rises

## Explanation

Capture every upward day-to-day price increase.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Peak-valley pairing.

## Common mistakes

Trying to track explicit buy/sell days.

## Learning notes

Unlimited transactions sum all positive deltas.

## Solution

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

```
