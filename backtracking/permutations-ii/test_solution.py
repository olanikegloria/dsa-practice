from solution import Solution

def test_112():
    result = Solution().permuteUnique([1, 1, 2])
    assert sorted(map(tuple, result)) == sorted(map(tuple, [[1, 1, 2], [1, 2, 1], [2, 1, 1]]))

def test_single():
    assert Solution().permuteUnique([0]) == [[0]]
