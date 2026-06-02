from schemas.content_schema import ContentResponse


def parse_ai_response(response_text):

    captions = []
    hashtags = []
    ideas = []

    current_section = None

    for line in response_text.splitlines():

        clean = line.strip()

        if not clean:
            continue

        lower = clean.lower()

        if lower.startswith("captions"):
            current_section = "captions"
            continue

        elif lower.startswith("hashtags"):
            current_section = "hashtags"
            continue

        elif lower.startswith("ideas"):
            current_section = "ideas"
            continue

        if current_section == "captions":
            captions.append(clean)

        elif current_section == "hashtags":
            hashtags.append(clean)

        elif current_section == "ideas":
            ideas.append(clean)

    return ContentResponse(captions=captions, hashtags=hashtags, ideas=ideas)
