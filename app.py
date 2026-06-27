from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="frontend")


@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/style.css")
def style():
    return send_from_directory("frontend", "style.css")


@app.route("/script.js")
def script():
    return send_from_directory("frontend", "script.js")


if __name__ == "__main__":
    app.run(debug=True)