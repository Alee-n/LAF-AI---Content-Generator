from services.parsing_service import parse_ai_response


def test_parse_response():

    sample = """
Captions:
Caption One
Caption Two

Hashtags:
#one
#two

Ideas:
Idea One
Idea Two
"""

    result = parse_ai_response(sample)

    assert len(result.captions) > 0
    assert len(result.hashtags) > 0
    assert len(result.ideas) > 0
