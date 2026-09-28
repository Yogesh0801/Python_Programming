from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return render_template("home.html")
    name = " Yogesh bandewar"
    return render_template("home.html", name = name)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/courses")
def courses():
    # return render_template("courses.html")
    courses = [
        "Python",
        "Flask",
        "Data Science",
        "Machine Learning",
        "AI"
    ]
    return render_template("courses.html", courses=courses)


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/trainer")
def trainer():

    name = "Yogesh"
    subject = "Flask"
    experience = 5

    return render_template(
        "trainer.html",
        name=name,
        subject=subject,
        experience=experience
    )

if __name__ == "__main__":
    app.run(debug=True)