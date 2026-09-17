from solution import Solution

def test_three_rows():
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_one_row():
    assert Solution().convert("ABC", 1) == "ABC"
