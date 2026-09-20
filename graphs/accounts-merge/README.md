# Accounts Merge

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/accounts-merge/

## Problem

Given a list of accounts where each element accounts[i] is a list of strings, merge the accounts of the same person. Return the accounts in any order.

## Approach

Union-Find on emails

## Explanation

Union emails within each account; group by root and sort.

## Complexity

- Time: O(n log n) for sorting emails
- Space: O(n)

## Alternatives

DFS on email graph.

## Common mistakes

Not linking all emails to the first email in account.

## Learning notes

Treat emails as graph nodes shared across accounts.

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            first = acc[1]
            for em in acc[1:]:
                email_to_name[em] = name
                union(first, em)

        groups = defaultdict(set)
        for em in email_to_name:
            groups[find(em)].add(em)

        res = []
        for root in groups:
            emails = sorted(groups[root])
            res.append([email_to_name[emails[0]]] + emails)
        return res

```
