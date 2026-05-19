def initialize_analytics(session):

    if "history" not in session:

        session["history"] = []

    if "generation_count" not in session:

        session["generation_count"] = 0


def update_analytics(session, business, audience, emotion):

    session["generation_count"] += 1

    session["last_business"] = business

    session["last_audience"] = audience

    session["last_emotion"] = emotion
