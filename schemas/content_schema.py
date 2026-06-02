class ContentResponse:

    def __init__(self, captions=None, hashtags=None, ideas=None):

        self.captions = captions or []

        self.hashtags = hashtags or []

        self.ideas = ideas or []

    def to_dict(self):

        return {
            "captions": self.captions,
            "hashtags": self.hashtags,
            "ideas": self.ideas,
        }
