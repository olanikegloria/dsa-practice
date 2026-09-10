from solution import Codec

def test_roundtrip():
    codec = Codec()
    words = ["lint", "code", "", "love#you"]
    assert codec.decode(codec.encode(words)) == words
