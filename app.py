from flask import Flask, render_template, request

app = Flask(__name__)

MOCK_WEATHER = {
    "New York": {"temperature": -2, "condition": "Snowy"},
    "Los Angeles": {"temperature": 15, "condition": "Sunny"},
    "Chicago": {"temperature": -5, "condition": "Freezing"},
}

WINTER_FACTS = [
    "The coldest temperature ever recorded was -128.6°F (-89.2°C) in Antarctica.",
    "Snowflakes are made up of ice crystals, and no two snowflakes are alike.",
    "Winter is caused by the Earth tilting away from the Sun.",
    "Polar bears are born during the winter months."
]

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    selected_fact = WINTER_FACTS[0]
    city = ""

    if request.method == "POST":
        city = request.form.get("city")
        weather = MOCK_WEATHER.get(city, {"temperature": "N/A", "condition": "Unknown"})
        selected_fact = WINTER_FACTS[len(city) % len(WINTER_FACTS)]

    return render_template("index.html", weather=weather, city=city, fact=selected_fact)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
