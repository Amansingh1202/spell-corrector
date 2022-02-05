from flask import Flask, render_template, request, jsonify, make_response

from spellchecker import SpellChecker

spell = SpellChecker()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check-spell", methods=["POST"])
def checkSpell():
    req = request.get_json()
    values = req["message"].split(" ")
    output = []
    for val in values:
        output.append(spell.correction(val))
    correctVal = " ".join(output)
    ans = {"message": correctVal}
    res = make_response(jsonify(ans), 200)
    return res


if __name__ == "__main__":
    app.run()
