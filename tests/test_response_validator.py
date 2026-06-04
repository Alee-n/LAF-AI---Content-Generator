from schemas.content_schema import ContentResponse

from services.response_validation_service import ResponseValidator


def test_response_validator():

    response = ContentResponse(

        captions=["Caption"],

        hashtags=["#test"],

        ideas=["Idea"]

    )

    assert ResponseValidator.validate(response)

def test_invalid_response():

    response = ContentResponse()

    assert ResponseValidator.validate(response) is False