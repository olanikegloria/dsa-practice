from solution import Solution

def test_example():
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    Solution().wallsAndGates(rooms)
    assert rooms[0][3] == 1 and rooms[2][2] == 2
