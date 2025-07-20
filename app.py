# app.py

from flask import Flask, render_template, request
import datetime
from lurelogic_core import recommend_lure

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        fish = request.form.get("fish")
        cloud_cover = request.form.get("cloud")
        water_clarity = request.form.get("clarity")
        now = datetime.datetime.now()

        try:
            result = recommend_lure(fish, now, cloud_cover, water_clarity)
        except ValueError as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)