from flask import Flask, render_template, request, session

from config import Config

from content_engine import generate_dynamic_content, process_content

from analytics import initialize_analytics, update_analytics

from ai_engine import generate_ai_content

app = Flask(__name__)

# CONFIGURATION

app.config.from_object(Config)

app.secret_key = Config.SECRET_KEY


# HOME ROUTE


@app.route("/", methods=["GET", "POST"])
def home():

    # INITIALIZE ANALYTICS

    initialize_analytics(session)

    # DEFAULT VALUES

    result = None

    error = None

    business = "bakery"

    platform = "Instagram"

    tone = "Casual"

    market = "Global"

    language = "English"

    audience = "Students"

    season = "Summer"

    emotion = "Exciting"

    platform_tip = ""

    # FORM SUBMISSION

    if request.method == "POST":

        # GET FORM DATA

        business = request.form.get("business")

        platform = request.form.get("platform")

        tone = request.form.get("tone")

        market = request.form.get("market")

        language = request.form.get("language")

        audience = request.form.get("audience")

        season = request.form.get("season")

        emotion = request.form.get("emotion")

        # VALIDATION

        if not business:

            error = "Please select a business type."

        else:

            # GENERATE CONTENT

            result = generate_dynamic_content(business)

            # PROCESS PERSONALIZATION

            result = process_content(result, language, audience, season, emotion)

            # OPTIONAL AI PREVIEW
            # (FOR FUTURE GEMINI INTEGRATION)

            ai_preview = generate_ai_content(
                business, audience, emotion, season, language
            )

            print(ai_preview)

            # PLATFORM TIPS

            if platform == "Instagram":

                platform_tip = (
                    "Use short captions, "
                    "strong visuals, and reels "
                    "for better engagement."
                )

            elif platform == "YouTube":

                platform_tip = (
                    "Use storytelling, hooks, "
                    "and audience retention "
                    "strategies for better reach."
                )

            # UPDATE ANALYTICS

            update_analytics(session, business, audience, emotion)

            # STORE HISTORY

            history_item = {"business": business, "captions": result["captions"]}

            session["history"].append(history_item)

            session.modified = True

    # RENDER TEMPLATE

    return render_template(
        "index.html",
        result=result,
        error=error,
        business=business,
        platform=platform,
        tone=tone,
        market=market,
        language=language,
        audience=audience,
        season=season,
        emotion=emotion,
        platform_tip=platform_tip,
        history=session.get("history", []),
        generation_count=session.get("generation_count", 0),
    )


# RUN APPLICATION

if __name__ == "__main__":

    app.run(debug=True)
