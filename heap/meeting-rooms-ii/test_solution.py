from solution import Solution

def test_example():
    assert Solution().minMeetingRooms([[0,30],[5,10],[15,20]]) == 2

def test_chain():
    assert Solution().minMeetingRooms([[1,2],[2,3],[3,4]]) == 1
