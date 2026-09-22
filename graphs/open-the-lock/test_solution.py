from solution import Solution

def test_example():
    dead = ["0201", "0101", "0102", "1212", "2002"]
    assert Solution().openLock(dead, "0202") == 6

def test_already():
    assert Solution().openLock(["8888"], "0009") == 1
