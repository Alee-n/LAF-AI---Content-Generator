from schemas.content_schema import ContentResponse


def test_content_response_valid():

    response = ContentResponse(

        captions=["Caption"],

        hashtags=["#test"],

        ideas=["Idea"]

    )

    assert response.is_valid is True


def test_content_response_invalid():

    response = ContentResponse()

    assert response.is_valid is False