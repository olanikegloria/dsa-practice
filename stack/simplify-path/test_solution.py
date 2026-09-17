from solution import Solution

def test_home():
    assert Solution().simplifyPath("/home/") == "/home"

def test_parent():
    assert Solution().simplifyPath("/../") == "/"

def test_dots():
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"
