# Candy

**Topic:** arrays  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/candy/

## Problem

There are n children standing in a line with ratings[i]. Each child must have at least one candy, and children with a higher rating get more candy than neighbors. Return the minimum number of candies needed.

## Approach

Two-pass greedy

## Explanation

Left-to-right then right-to-left passes enforce neighbor constraints.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Peaks and valleys counting.

## Common mistakes

Only scanning one direction.

## Learning notes

Take max from both directions for hills.

## Solution

```python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

```
