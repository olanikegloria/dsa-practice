from solution import Solution

def test_323():
    assert Solution().majorityElement([3, 2, 3]) == [3]

def test_122333():
    assert sorted(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])) == [1, 2]
