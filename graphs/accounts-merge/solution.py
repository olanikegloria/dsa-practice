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
