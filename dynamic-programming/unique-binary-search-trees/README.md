# Unique Binary Search Trees

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/unique-binary-search-trees/

## Problem

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

## Approach

Dynamic programming

## Explanation

Catalan DP: choose root r, multiply left and right subtree counts.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Alternatives

Direct Catalan formula.

## Common mistakes

Off-by-one on subtree sizes.

## Learning notes

Classic counting DP on BST structure.

## Solution

```python
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[n]

```
