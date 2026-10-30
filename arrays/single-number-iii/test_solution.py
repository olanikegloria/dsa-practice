from solution import Solution

def test_example():
    assert sorted(Solution().singleNumber([1, 2, 1, 3, 2, 5])) == [3, 5]

def test_two_singles():
    assert sorted(Solution().singleNumber([1, 2])) == [1, 2]
