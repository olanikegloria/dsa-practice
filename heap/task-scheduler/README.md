# Task Scheduler

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/task-scheduler/

## Problem

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there is a constraint: identical tasks must be separated by at least n intervals. Return the minimum number of intervals required to complete all tasks.

## Approach

Closed-form from the most frequent task

## Explanation

The busiest task lays down (maxf - 1) full cool-down frames. Idle slots fill with other tasks, and leftover work just appends.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

A max-heap simulation of the cool-down queue.

## Common mistakes

Forgetting that the answer cannot be shorter than the number of tasks.

## Learning notes

Idle time only appears when the cool-down frames outgrow the remaining work.

## Solution

```python
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        maxf = max(counts)
        ties = counts.count(maxf)
        return max(len(tasks), (maxf - 1) * (n + 1) + ties)

```
