from schemas.content_schema import ContentResponse


def test_schema_validity():

    result = ContentResponse(

        captions=["A"],

        hashtags=["#A"],

        ideas=["Idea"]

    )

    assert result.is_valid is True