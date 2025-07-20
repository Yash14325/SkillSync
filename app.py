# app.py
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        skill = request.form["skill"].lower()
        # Dummy matching logic
        if "python" in skill:
            result = "Recommended: Backend Intern at CodeStartup"
        elif "ui" in skill:
            result = "Recommended: UI/UX Designer at DesignLab"
        else:
            result = "No match found currently."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
