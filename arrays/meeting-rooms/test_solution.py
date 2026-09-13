from solution import Solution

def test_false():
    assert Solution().canAttendMeetings([[0,30],[5,10],[15,20]]) is False

def test_true():
    assert Solution().canAttendMeetings([[7,10],[2,4]]) is True
