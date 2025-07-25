from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    chosen = None
    if request.method == "POST":
        chosen = request.form.get("zone")
    return render_template("index.html", selected=chosen)

if __name__ == "__main__":
    app.run(debug=True)

