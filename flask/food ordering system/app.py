from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_ordering"
)

# Read all foods
@app.route("/")
def foods():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM foods")

    data = cursor.fetchall()

    cursor.close()

    return render_template("foods.html", foods=data)

# add food
@app.route("/add", methods=["GET", "POST"])
def add_food():

    if request.method == "POST":

        food_name = request.form["food_name"]
        category = request.form["category"]
        price = request.form["price"]
        description = request.form["description"]

        cursor = db.cursor()

        query = """
        INSERT INTO foods
        (food_name, category, price, description)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            food_name,
            category,
            price,
            description
        )

        cursor.execute(query, values)

        db.commit()

        cursor.close()

        return "Food Added Successfully"

    return render_template("add_food.html")

# update food
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_food(id):

    cursor = db.cursor()

    if request.method == "POST":

        food_name = request.form["food_name"]
        category = request.form["category"]
        price = request.form["price"]
        description = request.form["description"]

        query = """
        UPDATE foods
        SET food_name=%s,
            category=%s,
            price=%s,
            description=%s
        WHERE food_id=%s
        """

        values = (
            food_name,
            category,
            price,
            description,
            id
        )

        cursor.execute(query, values)

        db.commit()

        cursor.close()

        return "Food Updated Successfully"

    cursor.execute(
        "SELECT * FROM foods WHERE food_id=%s",
        (id,)
    )

    food = cursor.fetchone()

    cursor.close()

    return render_template(
        "edit_food.html",
        food=food
    )

@app.route("/delete/<int:id>")
def delete_food(id):

    cursor = db.cursor()

    query = "DELETE FROM foods WHERE food_id=%s"

    cursor.execute(query, (id,))

    db.commit()

    cursor.close()

    return "Food Deleted Successfully"

if __name__ == "__main__":
    app.run(debug=True)