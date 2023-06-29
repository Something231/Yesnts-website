from flask import Flask, redirect, url_for, render_template, request, session, flash
from replit import db

app = Flask('__main__')
app.secret_key = "sniff"


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/home")
def rhom():
  return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    user = request.form["nm"]
    if user in db:
      password = request.form["pcode"]
      if db[user] == [password]:
        session["user"] = user
        flash("Login successful")
        return redirect(url_for("user"))
      else:
        flash("Incorrect username or password")
        return redirect(url_for("login"))
    else:
      flash("Incorrect username or password")
      return redirect(url_for("login"))
  else:
    if "user" in session:
      flash("Already logged in!")
      return redirect(url_for("user"))
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
  if request.method == "POST":
    user = request.form["nm"]
    if user in db:
      flash("Account already exists!")
      return redirect(url_for('register'))
    password = request.form["pcode"]
    db[user] = [password]
    flash("Account Created - Please sign in")
    return redirect(url_for("login"))
  else:
    if "user" in session:
      flash("Already Logged in!")
      return redirect(url_for("user"))
    return render_template("register.html")


@app.route("/user")
def user():
  if "user" in session:
    user = session["user"]
    return render_template("user.html", user=user)
  else:
    flash("You are not logged in!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
  if "user" in session:
    user = session["user"]
    flash(f"You have been logged out, {user}", "info")
  else:
    flash("You are not logged in!")
  session.pop("user", None)
  return redirect(url_for("login"))


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
