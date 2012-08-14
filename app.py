from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Nothing to see here...."

@app.route("/log", method=["POST"])
def log():
    """
    * parse post data
    * Check config for type of logging...
    * save to DB or log....
    """

    message = request.form["message"]

    return "logging...."

if __name__ == "__main__":
    app.run()
