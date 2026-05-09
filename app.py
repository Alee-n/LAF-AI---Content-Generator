from flask import Flask, render_template, request, session
import random
import time

app = Flask(__name__)

# SECRET KEY FOR SESSION STORAGE
app.secret_key = "laf_ai_secret"


# DYNAMIC CONTENT GENERATOR
def generate_dynamic_content(category):

    random.seed(time.time())

    data = {

        "bakery": {
            "items": [
                "croissants",
                "cakes",
                "bread",
                "pastries",
                "cookies",
                "brownies"
            ],

            "adjectives": [
                "fresh",
                "soft",
                "delicious",
                "sweet",
                "warm",
                "fluffy"
            ],

            "actions": [
                "grab",
                "try",
                "taste",
                "enjoy",
                "experience"
            ],

            "times": [
                "today",
                "this evening",
                "right now",
                "this weekend"
            ],

            "vibes": [
                "comfort",
                "happiness",
                "sweet moments",
                "pure joy"
            ]
        },

        "restaurant": {
            "items": [
                "dishes",
                "meals",
                "plates",
                "specials",
                "menu"
            ],

            "adjectives": [
                "rich",
                "authentic",
                "flavorful",
                "premium",
                "satisfying"
            ],

            "actions": [
                "try",
                "explore",
                "discover",
                "enjoy",
                "experience"
            ],

            "times": [
                "tonight",
                "this weekend",
                "today",
                "with friends"
            ],

            "vibes": [
                "fine dining",
                "great taste",
                "food journey",
                "perfect dinner"
            ]
        },

        "travel": {
            "items": [
                "destinations",
                "places",
                "trips",
                "journeys",
                "locations"
            ],

            "adjectives": [
                "beautiful",
                "breathtaking",
                "exciting",
                "peaceful",
                "unique"
            ],

            "actions": [
                "explore",
                "visit",
                "discover",
                "travel",
                "experience"
            ],

            "times": [
                "this season",
                "now",
                "your next trip",
                "soon"
            ],

            "vibes": [
                "adventure",
                "freedom",
                "memories",
                "exploration"
            ]
        },

        "convenience store": {
            "items": [
                "snacks",
                "groceries",
                "drinks",
                "daily essentials",
                "quick items"
            ],

            "adjectives": [
                "quick",
                "easy",
                "fast",
                "simple",
                "reliable"
            ],

            "actions": [
                "grab",
                "get",
                "pick",
                "buy",
                "find"
            ],

            "times": [
                "anytime",
                "24/7",
                "right now",
                "near you"
            ],

            "vibes": [
                "convenience",
                "speed",
                "ease",
                "daily comfort"
            ]
        }
    }

    if category not in data:

        return {
            "captions": [
                "Great content coming soon 🚀"
            ],

            "hashtags": [
                "#Content"
            ],

            "ideas": [
                "General promotion idea"
            ]
        }

    cat = data[category]

    # CAPTION STYLES

    def style_1():
        return f"{random.choice(cat['actions']).capitalize()} our {random.choice(cat['adjectives'])} {random.choice(cat['items'])} {random.choice(cat['times'])}! ✨"

    def style_2():
        return f"{random.choice(cat['adjectives']).capitalize()} {random.choice(cat['items'])} that bring {random.choice(cat['vibes'])} — {random.choice(cat['actions'])} them now! 😍"

    def style_3():
        return f"Looking for {random.choice(cat['adjectives'])} {random.choice(cat['items'])}? {random.choice(cat['actions']).capitalize()} them {random.choice(cat['times'])}! 🔥"

    def style_4():
        return f"{random.choice(cat['items']).capitalize()} + {random.choice(cat['vibes'])} = your perfect moment. {random.choice(cat['actions']).capitalize()} it {random.choice(cat['times'])}! 💫"

    def style_5():
        return f"Don't miss our {random.choice(cat['adjectives'])} {random.choice(cat['items'])} — {random.choice(cat['actions'])} yours {random.choice(cat['times'])}! 🚀"

    generators = [
        style_1,
        style_2,
        style_3,
        style_4,
        style_5
    ]

    captions = [
        random.choice(generators)()
        for _ in range(3)
    ]

    # HASHTAGS

    base_tags = {

        "bakery": [
            "#BakeryLife",
            "#FreshBakes",
            "#SweetTreats"
        ],

        "restaurant": [
            "#FoodLovers",
            "#DineOut",
            "#FoodExperience"
        ],

        "travel": [
            "#TravelLife",
            "#ExploreMore",
            "#Wanderlust"
        ],

        "convenience store": [
            "#QuickShopping",
            "#DailyNeeds",
            "#EasyLife"
        ]
    }

    global_tags = [
        "#TrendingNow",
        "#ContentMarketing",
        "#GrowOnline",
        "#DigitalSuccess",
        "#BrandBuilding",
        "#MarketingTips",
        "#ViralContent",
        "#OnlineBusiness"
    ]

    hashtags = random.sample(
        base_tags[category] + global_tags,
        3
    )

    # IDEAS

    idea_formats = [

        lambda:
        f"Show {random.choice(cat['items'])} preparation in a short video",

        lambda:
        f"Create a reel featuring {random.choice(cat['vibes'])}",

        lambda:
        f"Record customer reactions to your {random.choice(cat['items'])}",

        lambda:
        f"Post a day-in-life content around your {category}",

        lambda:
        f"Make a quick tips video about {random.choice(cat['items'])}",

        lambda:
        f"Show before and after experience of customers",

        lambda:
        f"Highlight best-selling {random.choice(cat['items'])}",

        lambda:
        f"Create engaging story polls about {random.choice(cat['items'])}"
    ]

    ideas = [
        random.choice(idea_formats)()
        for _ in range(2)
    ]

    return {
        "captions": captions,
        "hashtags": hashtags,
        "ideas": ideas
    }


# JAPAN MODE
def japan_mode(content):

    return (
        content +
        " 🇯🇵 | Inspired by Japanese minimalism."
    )


# HOME ROUTE
@app.route('/', methods=['GET', 'POST'])
def home():

    result = None

    business = ""
    platform = "Instagram"
    tone = "Casual"
    market = "Global"

    platform_tip = ""
    error = ""

    # HISTORY SESSION
    if "history" not in session:
        session["history"] = []

    if request.method == 'POST':

        business = request.form.get(
            'business'
        ).strip().lower()

        platform = request.form.get(
            'platform'
        )

        tone = request.form.get(
            'tone'
        )

        market = request.form.get(
            'market'
        )

        if not business:

            error = "Please select business type"

        else:

            result = generate_dynamic_content(
                business
            )

            # JAPAN MODE
            if market == "Japan":

                result["captions"] = [

                    japan_mode(c)

                    for c in result["captions"]
                ]

            # PLATFORM TIPS
            if platform == "Instagram":

                platform_tip = (
                    "Use Reels and trending audio 📈"
                )

            else:

                platform_tip = (
                    "Use Shorts and consistent uploads 🚀"
                )

            # SAVE HISTORY
            history = session["history"]

            history.insert(0, {

                "business": business,
                "captions": result["captions"]
            })

            # LIMIT HISTORY
            history = history[:5]

            session["history"] = history

    return render_template(

        "index.html",

        result=result,

        business=business,
        platform=platform,
        tone=tone,
        market=market,

        platform_tip=platform_tip,
        error=error,

        history=session["history"]
    )


if __name__ == "__main__":
    app.run(debug=True)