from solution import Solution

def test_example():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]

def test_single():
    assert Solution().partitionLabels("eccbbbbdec") == [10]
