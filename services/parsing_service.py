from schemas.content_schema import ContentResponse


def parse_ai_response(response_text):

    captions = []

    hashtags = []

    ideas = []

    current_section = None

    lines = response_text.split("\n")

    for line in lines:

        clean = line.strip()

        if not clean:

            continue

        lower = clean.lower()

        if "caption" in lower:

            current_section = "captions"

            continue

        elif "hashtag" in lower:

            current_section = "hashtags"

            continue

        elif "idea" in lower:

            current_section = "ideas"

            continue

        if current_section == ("captions"):

            captions.append(clean)

        elif current_section == ("hashtags"):

            hashtags.append(clean)

        elif current_section == ("ideas"):

            ideas.append(clean)

    return ContentResponse(captions, hashtags, ideas)
