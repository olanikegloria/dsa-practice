from solution import Solution

def test_example():
    out = Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
    assert out == ["i", "love"]

def test_tie():
    out = Solution().topKFrequent(["a", "aa", "aaa"], 2)
    assert out == ["a", "aa"]
