from flask import Flask, render_template, request
from data_fetcher import get_today_slots   # ← NEW: pulls slots from JSON/mock
# -----------------------------------------------------------------------------
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    slots = []          # list of 1-hour ranges, e.g. ["04:00-05:00", …]
    zone  = None        # which zone the user picked

    if request.method == "POST":
        zone   = request.form["zone"]          # dropdown value
        result = get_today_slots(zone)         # call helper
        slots  = result["slots"]               # extract list

    # pass data to Jinja template
    return render_template("index.html", selected=zone, slots=slots)


if __name__ == "__main__":
    app.run(debug=True)

