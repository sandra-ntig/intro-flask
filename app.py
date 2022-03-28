from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #name = request.form.get("name")
        #age = request.form.get("age")
        form = request.form
        user = {
            "name": form['name'],
            "age": int(form['age'])
        }
    return render_template("home.html", user=user)


@app.route('/expressions')
def expressions():

    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template("expressions.html", **kwargs)


@app.route("/data-structures/")
def render_data_structures():

    movies = ["Frost", "Top Gun", "Sound of Music"
              ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    return render_template("data_structures.html", movies=movies, car=car)


@app.route("/conditional-basics/")
def render_conditional_basics():

    company = "Microsoft"

    return render_template("conditional_basics.html", company=company)


@app.route("/for-loop/")
def render_loops():

    planets = ["Mercury", "Venus", "Tellus", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    return render_template("for-loops.html", planets=planets)
