from flask import Flask, render_template, request, redirect, url_for, session
import re
from datetime import datetime
from google import genai
client = genai.Client(api_key="AIzaSyAMF1ACNKHg3DRt7EVs1z_ccI6PPtAHIJ8")

app = Flask(__name__)
app.secret_key = "placement_secret"

# Temporary user storage
users = {}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern,email):
            return render_template("register.html",error="Enter valid email!")

        users[username] = {
            "email":email,
            "password":password
        }

        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("select_branch"))

        return render_template("login.html",error="Invalid Credentials")

    return render_template("login.html")

# ---------------- SELECT BRANCH ----------------
@app.route("/select-branch", methods=["GET","POST"])
def select_branch():

    if request.method == "POST":
        session["branch"] = request.form.get("branch")
        return redirect(url_for("dashboard"))

    return render_template("select_branch.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    branch = session.get("branch")

    if branch == "cse":
        return render_template("cse/dashboard.html")

    elif branch == "ece":
        return render_template("ece/dashboard.html")

    elif branch == "mech":
        return render_template("mech/dashboard.html")

    elif branch == "EEE":
        return render_template("EEE/dashboard.html")

    elif branch == "CIVIL":
        return render_template("CIVIL/dashboard.html")

    return redirect(url_for("select_branch"))

# ---------------- GOAL TRACKER ----------------
@app.route("/goals")
def goals():
    return render_template("goal_tracker.html")

# ---------------- STUDY PLAN ----------------
@app.route("/studyplan")
def studyplan():
    return render_template("studyplan.html")



@app.route("/ai", methods=["GET","POST"])
def ai():

    answer = ""
    question = ""

    if request.method == "POST":

        question = request.form.get("question")

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=question
            )

            answer = response.text

        except Exception as e:
            answer = "AI Error: " + str(e)

    return render_template("ai_chatbot.html", answer=answer, question=question)
# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)