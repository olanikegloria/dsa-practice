# Implement Trie (Prefix Tree)

**Topic:** hash-maps  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/implement-trie-prefix-tree/

## Problem

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the Trie class with insert, search, and startsWith methods.

## Approach

Trie with dict children

## Explanation

Trie nodes map char -> child; end flag marks complete words.

## Complexity

- Time: O(L) per operation
- Space: O(total chars)

## Alternatives

Array of 26 children.

## Common mistakes

Not setting end flag on insert.

## Learning notes

Trie prefix sharing saves space for dictionaries.

## Solution

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

```
