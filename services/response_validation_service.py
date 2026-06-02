from schemas.content_schema import ContentResponse


class ResponseValidator:

    @staticmethod
    def validate(response):

        if not isinstance(response, ContentResponse):
            return False

        if len(response.captions) == 0:

            return False

        if len(response.hashtags) == 0:

            return False

        if len(response.ideas) == 0:

            return False

        return True
