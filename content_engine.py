import random
import time

# JAPAN MODE


def japan_mode(content):

    return content + " 🇯🇵 | Inspired by Japanese minimalism."


# MAIN CONTENT GENERATOR


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
                "brownies",
            ],
            "adjectives": ["fresh", "soft", "delicious", "sweet", "warm", "fluffy"],
            "actions": ["grab", "try", "taste", "enjoy", "experience"],
            "times": ["today", "this evening", "right now", "this weekend"],
            "vibes": ["comfort", "happiness", "sweet moments", "pure joy"],
        },
        "restaurant": {
            "items": ["dishes", "meals", "plates", "specials", "menu"],
            "adjectives": ["rich", "authentic", "flavorful", "premium", "satisfying"],
            "actions": ["try", "explore", "discover", "enjoy", "experience"],
            "times": ["tonight", "this weekend", "today", "with friends"],
            "vibes": ["fine dining", "great taste", "food journey", "perfect dinner"],
        },
        "travel": {
            "items": ["destinations", "places", "trips", "journeys", "locations"],
            "adjectives": [
                "beautiful",
                "breathtaking",
                "exciting",
                "peaceful",
                "unique",
            ],
            "actions": ["explore", "visit", "discover", "travel", "experience"],
            "times": ["this season", "now", "your next trip", "soon"],
            "vibes": ["adventure", "freedom", "memories", "exploration"],
        },
        "convenience store": {
            "items": [
                "snacks",
                "groceries",
                "drinks",
                "daily essentials",
                "quick items",
            ],
            "adjectives": ["quick", "easy", "fast", "simple", "reliable"],
            "actions": ["grab", "get", "pick", "buy", "find"],
            "times": ["anytime", "24/7", "right now", "near you"],
            "vibes": ["convenience", "speed", "ease", "daily comfort"],
        },
    }

    if category not in data:

        return {
            "captions": ["Great content coming soon 🚀"],
            "hashtags": ["#Content"],
            "ideas": ["General promotion idea"],
        }

    cat = data[category]

    # CAPTION GENERATORS

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

    generators = [style_1, style_2, style_3, style_4, style_5]

    captions = [random.choice(generators)() for _ in range(3)]

    # HASHTAGS

    base_tags = {
        "bakery": ["#BakeryLife", "#FreshBakes", "#SweetTreats"],
        "restaurant": ["#FoodLovers", "#DineOut", "#FoodExperience"],
        "travel": ["#TravelLife", "#ExploreMore", "#Wanderlust"],
        "convenience store": ["#QuickShopping", "#DailyNeeds", "#EasyLife"],
    }

    global_tags = [
        "#TrendingNow",
        "#ContentMarketing",
        "#GrowOnline",
        "#DigitalSuccess",
        "#BrandBuilding",
        "#MarketingTips",
        "#ViralContent",
        "#OnlineBusiness",
    ]

    hashtags = random.sample(base_tags[category] + global_tags, 3)

    # IDEAS

    idea_formats = [
        lambda: f"Show {random.choice(cat['items'])} preparation in a short video",
        lambda: f"Create a reel featuring {random.choice(cat['vibes'])}",
        lambda: f"Record customer reactions to your {random.choice(cat['items'])}",
        lambda: f"Post a day-in-life content around your {category}",
        lambda: f"Make a quick tips video about {random.choice(cat['items'])}",
        lambda: f"Show before and after experience of customers",
        lambda: f"Highlight best-selling {random.choice(cat['items'])}",
        lambda: f"Create engaging story polls about {random.choice(cat['items'])}",
    ]

    ideas = [random.choice(idea_formats)() for _ in range(2)]

    return {"captions": captions, "hashtags": hashtags, "ideas": ideas}


def process_content(result, language, audience, season, emotion):

    # LANGUAGE

    if language == "Japanese Style":

        result["captions"] = [japan_mode(c) for c in result["captions"]]

    # AUDIENCE

    if audience == "Students":

        result["captions"] = [
            c + " 🎓 Perfect for student lifestyle." for c in result["captions"]
        ]

    elif audience == "Professionals":

        result["captions"] = [
            c + " 💼 Designed for busy professionals." for c in result["captions"]
        ]

    elif audience == "Tourists":

        result["captions"] = [
            c + " ✈️ Great for travelers and explorers." for c in result["captions"]
        ]

    elif audience == "Families":

        result["captions"] = [
            c + " 👨‍👩‍👧 Ideal for family experiences." for c in result["captions"]
        ]

    # SEASON

    if season == "Summer":

        result["captions"] = [
            c + " ☀️ Summer vibes included." for c in result["captions"]
        ]

    elif season == "Winter":

        result["captions"] = [
            c + " ❄️ Cozy winter atmosphere." for c in result["captions"]
        ]

    elif season == "Spring":

        result["captions"] = [
            c + " 🌸 Fresh spring energy." for c in result["captions"]
        ]

    elif season == "Autumn":

        result["captions"] = [
            c + " 🍂 Warm autumn feeling." for c in result["captions"]
        ]

    # EMOTION

    if emotion == "Exciting":

        result["captions"] = [
            c + " 🔥 High-energy experience!" for c in result["captions"]
        ]

    elif emotion == "Calm":

        result["captions"] = [
            c + " 🌿 Relaxing and peaceful." for c in result["captions"]
        ]

    elif emotion == "Luxury":

        result["captions"] = [
            c + " ✨ Premium luxury feel." for c in result["captions"]
        ]

    elif emotion == "Friendly":

        result["captions"] = [c + " 😊 Warm and welcoming." for c in result["captions"]]

    return result
