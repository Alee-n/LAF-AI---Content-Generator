from flask import Flask, render_template, request, session

from config import Config

from content_engine import generate_dynamic_content, process_content

from analytics import initialize_analytics, update_analytics

from ai_engine import generate_ai_content

from services.parsing_service import parse_ai_response

from services.validation_service import (validate_business,validate_ai_mode,validate_language)

from services.logging_service import log_generation, log_error, log_provider

from services.response_validation_service import ResponseValidator

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

    ai_mode = "Creative"

    platform_tip = ""

    # FORM SUBMISSION

    if request.method == "POST":

        # GET FORM DATA

        business = request.form.get("business")

        print("Business received:", business)

        platform = request.form.get("platform")

        tone = request.form.get("tone")

        market = request.form.get("market")

        language = request.form.get("language")

        audience = request.form.get("audience")

        season = request.form.get("season")

        emotion = request.form.get("emotion")

        ai_mode = request.form.get("ai_mode")

        # VALIDATION

        if not validate_business(business):
            error = ("Invalid business type.")

        else:

            # AI GENERATION + PARSING

            try:

                log_generation(business, ai_mode)
                ai_text = generate_ai_content(
                    business, audience, emotion, season, language, ai_mode
                )

                ai_result = parse_ai_response(ai_text)

                if not ResponseValidator.validate(ai_result):

                    raise ValueError("Invalid AI response structure")

                result = ai_result.to_dict()

            except Exception as e:

                log_error(str(e))

                # FALLBACK GENERATION

                result = generate_dynamic_content(business)

                result = process_content(result, language, audience, season, emotion)

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
        ai_mode=ai_mode,
        platform_tip=platform_tip,
        history=session.get("history", []),
        generation_count=session.get("generation_count", 0),
    )


# RUN APPLICATION

if __name__ == "__main__":
    print("BEFORE RUN")

    app.run(host="127.0.0.1", port=5000, debug=False)

    print("AFTER RUN")
