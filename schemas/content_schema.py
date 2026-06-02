class ContentResponse:

    def __init__(self, captions=None, hashtags=None, ideas=None):

        self.captions = captions or []

        self.hashtags = hashtags or []

        self.ideas = ideas or []

    @property
    def is_valid(self):

        return len(self.captions) > 0 and len(self.hashtags) > 0 and len(self.ideas) > 0

    def to_dict(self):

        return {
            "captions": self.captions,
            "hashtags": self.hashtags,
            "ideas": self.ideas,
        }
