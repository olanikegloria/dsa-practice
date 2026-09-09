from solution import Solution

def test_example():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    got = {tuple(x) for x in Solution().pacificAtlantic(heights)}
    assert got == {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}
