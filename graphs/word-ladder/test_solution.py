from solution import Solution

def test_example():
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5

def test_missing_end():
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
