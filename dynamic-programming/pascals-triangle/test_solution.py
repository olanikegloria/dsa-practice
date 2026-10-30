from solution import Solution

def test_five_rows():
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def test_one_row():
    assert Solution().generate(1) == [[1]]
