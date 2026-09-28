# Import the Flask class from the flask package.
# This is necessary because we need Flask to create our web application.
# Alternative: we could also import a different library or create a custom server,
# but Flask is used here to make web routing and responses easier.
from flask import Flask

# Create a Flask application instance.
# The Flask() object is the main app that handles routes, requests, and responses.
# __name__ is a special Python variable that tells Flask where the app is located.
# Alternative: we could name the variable anything else, for example: my_app = Flask(__name__)
# but then we would need to use my_app instead of app everywhere.
app = Flask(__name__)


# This decorator tells Flask that the function below should run when the user visits the homepage.
# The URL "/" means the root page, such as http://localhost:5000/
# Alternative route paths can also be used, for example: "/home" or "/index".
@app.route("/")
def home():
    # This function returns the response shown to the user in the browser.
    # Instead of returning a plain string, we could also return HTML, JSON, templates, or redirect responses.
    return "Hello Flask"


# @app.route("/")
# def home():
#     return """
#     <html>
#         <head>
#             <title>Home</title>
#         </head>
#         <body>
#             <h1>Welcome</h1>
#             <p>This is my website</p>
#         </body>
#     </html>
#     """
# This decorator creates another route for the /about page.
# When a user goes to http://localhost:5000/about, this function will run.
# Alternative: we can use a different URL such as "/about-us" or "/info".
@app.route("/about")
def about():
    # This is the content returned for the about page.
    # We could also return a template like render_template("about.html")
    # or return a JSON object if the app is an API.
    return "this is about page"

# This condition checks whether the file is being run directly by Python.
# If we run the file with: python app.py
# then __name__ will be "__main__" and the code inside this block will execute.
# If we import this file in another Python file, this block will not run automatically.
# Alternative: we can also run the application using the Flask command:
# flask run
# or by using app.run() in a different file, but this pattern is common and simple.
if __name__ == "__main__":
    # This starts the Flask development web server.
    # debug=True enables debug mode, which shows errors in the browser and reloads automatically.
    # Alternative options:
    # app.run()  -> runs without debug mode
    # app.run(debug=False) -> disables debugging
    # app.run(host="0.0.0.0", port=5000) -> makes it accessible on a network or custom port
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)