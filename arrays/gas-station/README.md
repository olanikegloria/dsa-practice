# Gas Station

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/gas-station/

## Problem

There are n gas stations along a circular route. You have a car with an unlimited gas tank and start at an empty station with cost[i] gas to travel from station i to i+1. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

## Approach

Greedy one pass

## Explanation

If total gas covers total cost, the start is where cumulative deficit resets.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Try every start (slow).

## Common mistakes

Not checking global gas vs cost first.

## Learning notes

Deficit segment cannot contain a valid start.

## Solution

```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

```
