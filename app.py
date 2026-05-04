from flask import Flask, render_template, request
import random
import time
random.seed(time.time())

app = Flask(__name__)

# 🔥 Content Generator Function
def generate_content(business, platform, tone):
    
    if business.lower() == "bakery":

        starters = ["Freshly baked", "Warm and delicious", "Made with love", "Taste the freshness"]
        endings = ["Come grab a bite!", "Visit today!", "Try it now!", "Experience the flavor!"]

        captions = [
            f"{random.choice(starters)} 🍞✨ {random.choice(endings)}",
            f"{random.choice(starters)} 🥐 {random.choice(endings)}",
            f"{random.choice(starters)} 🍩 {random.choice(endings)}"
        ]

        hashtags = [
            "#BakeryLove #FreshDaily",
            "#SweetTooth #BakedWithLove",
            "#FreshBread #LocalBakery"
        ]

        ideas = [
            "Show behind-the-scenes baking process",
            "Customer reactions video",
            "Fresh items coming out of oven"
        ]

        return {
            "captions": captions,
            "hashtags": random.sample(hashtags, 3),
            "ideas": random.sample(ideas, 2)
        }

# 🇯🇵 Japan Mode
def japan_mode(content):
    return content + " 🇯🇵 | Inspired by Japanese minimalism. Arigatou gozaimasu!"


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    business = ""
    platform = "Instagram"
    tone = "Casual"
    market = "Global"

    if request.method == 'POST':
        business = request.form.get('business', '')
        platform = request.form.get('platform', 'Instagram')
        tone = request.form.get('tone', 'Casual')
        market = request.form.get('market', 'Global')

        result = generate_content(business, platform, tone)

        if market == "Japan":
            result["captions"] = [japan_mode(c) for c in result["captions"]]

        if not business.strip():
           return render_template(
             'index.html',
              result=None,
              error="Please enter a business type",
              business=business,
              platform=platform,
              tone=tone,
              market=market
           )

    return render_template(
        'index.html',
        result=result,
        business=business,
        platform=platform,
        tone=tone,
        market=market
    )



if __name__ == '__main__':
    app.run(debug=True)