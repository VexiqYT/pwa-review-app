from flask import Flask, render_template, request, send_from_directory, redirect, session, url_for
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

# -----------------------------
# JSON Persistence Helpers
# -----------------------------

REVIEWS_FILE = "reviews.json"
USERS_FILE = "users.json"

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# -----------------------------
# Load persistent data
# -----------------------------

# users = { username: {email, password} }
users = load_json(USERS_FILE)

# reviews_data = [ {id, category, title, rating, review, owner} ]
reviews_data = load_json(REVIEWS_FILE)

# -----------------------------
# ROUTES
# -----------------------------

@app.route("/")
def home():
    return render_template("home.html", reviews=reviews_data)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        identifier = request.form["identifier"]  # email OR username
        password = request.form["password"]

        # Check username first
        if identifier in users and users[identifier]["password"] == password:
            session["user"] = identifier
            return redirect(url_for("home"))

        # Check email
        for username, data in users.items():
            if data["email"] == identifier and data["password"] == password:
                session["user"] = username
                return redirect(url_for("home"))

        return render_template("login.html", error="Invalid email/username or password")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        # Username already exists
        if username in users:
            return render_template("register.html", error="Username already exists")

        # Email already used
        for u in users.values():
            if u["email"] == email:
                return render_template("register.html", error="Email already registered")

        # Save new user
        users[username] = {
            "email": email,
            "password": password
        }
        save_json(USERS_FILE, users)

        session["user"] = username
        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        category = request.form.get("category", "games")
        title = request.form["title"]
        rating = float(request.form["rating"])
        review_text = request.form["review"]

        review_id = len(reviews_data)
        new_review = {
            "id": review_id,
            "category": category,
            "title": title,
            "rating": rating,
            "review": review_text,
            "owner": session["user"]
        }

        reviews_data.append(new_review)
        save_json(REVIEWS_FILE, reviews_data)

        return redirect(url_for("reviews"))

    return render_template("add_review.html")

@app.route("/reviews")
def reviews():
    category = request.args.get("category")
    if category:
        filtered = [r for r in reviews_data if r["category"] == category]
    else:
        filtered = reviews_data
    return render_template("reviews.html", reviews=filtered, category=category)

@app.route("/review/<int:review_id>")
def review_details(review_id):
    review = next((r for r in reviews_data if r["id"] == review_id), None)
    if not review:
        return "Review not found", 404
    return render_template("review_details.html", review=review)

@app.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = next((r for r in reviews_data if r["id"] == review_id), None)
    if not review:
        return "Review not found", 404

    if session.get("user") != review["owner"]:
        return "Not allowed", 403

    if request.method == "POST":
        review["title"] = request.form["title"]
        review["rating"] = float(request.form["rating"])
        review["review"] = request.form["review"]

        save_json(REVIEWS_FILE, reviews_data)
        return redirect(url_for("review_details", review_id=review_id))

    return render_template("edit_review.html", review=review)

@app.route("/delete/<int:review_id>")
def delete_review(review_id):
    review = next((r for r in reviews_data if r["id"] == review_id), None)
    if not review:
        return "Review not found", 404

    if session.get("user") != review["owner"]:
        return "Not allowed", 403

    reviews_data.remove(review)
    save_json(REVIEWS_FILE, reviews_data)

    return redirect(url_for("reviews"))

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service_worker.js')
def service_worker():
    return send_from_directory('.', 'service_worker.js')

@app.route("/offline.html")
def offline():
    return render_template("offline.html")

if __name__ == "__main__":
    app.run(debug=True)
