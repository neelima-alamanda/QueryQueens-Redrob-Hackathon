from flask import Flask, send_from_directory, jsonify, send_file
import subprocess
import csv

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


@app.route("/rank", methods=["POST"])
def rank():

    subprocess.run(["python", "src/main.py"])

    results = []

    with open("submission.csv", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            results.append(row)

    return jsonify(results)

@app.route("/download")
def download():

    return send_file(
        "submission.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)