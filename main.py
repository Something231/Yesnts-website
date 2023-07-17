from flask import Flask, redirect, url_for, render_template, request, session, flash
from replit import db
import secrets
import json
import plotly.graph_objects as go

app = Flask('__main__')
app.secret_key = secrets.token_hex(16)


def write_to_json(data, filename):
  with open(filename, 'r+') as file:
    messages = json.load(file)
    messages.append(data)
    file.seek(0)
    json.dump(messages, file, indent=4)
    file.truncate()


def read_from_json(filename):
  with open(filename, 'r') as file:
    messages = json.load(file)
  contents = [message['content'] for message in messages]
  return contents

# sniff
@app.route("/")
def home():
  if "user" in session:
    user = session["user"]
    messages = read_from_json("admins.json")
    if user in messages:
      EE = "yes"
    else:
      EE = "nono"
    return render_template("index.html", coconut=EE)
  else:
    return render_template("index2.html")


@app.route("/home")
def rhom():
  return redirect(url_for("home"))


@app.route("/admin", methods=["POST", "GET"])
def adminpg():
  if request.method == "POST":
    question = request.form['question']
    responses = request.form.getlist('response')
    vote_counts = {response: 0 for response in responses}
    poll_data = {'question': question, 'responses': vote_counts}
    with open('poll_data.json', 'w') as file:
      json.dump(poll_data, file)
    with open('voting_status.json', 'w') as file:
      json.dump({}, file)
    flash("Poll created successfully!")
    return redirect(url_for("adminpg"))
  else:
    if "user" in session:
      user = session["user"]
      messages = read_from_json("admins.json")
      if user in messages:
        return render_template("admin.html", user=user)
      else:
        flash("You are not qualified to access that page!")
        return redirect(url_for("home"))
    else:
      flash("You need to be logged in to use this!")
      return redirect(url_for("login"))


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


@app.route("/chat", methods=["POST", "GET"])
def chat():
  if request.method == "POST":
    user = session["user"]
    mxg = request.form["mxg"]
    joinedm = ": ".join([user, mxg])
    joinedm = {'content': joinedm}
    write_to_json(joinedm, "chat.json")
    return redirect(url_for("chat"))
  else:
    if "user" in session:
      user = session["user"]
      messages = read_from_json('chat.json')
      return render_template("chat.html", user=user, hist=messages)
    else:
      flash("You need to be logged in to use chat!")
      return redirect(url_for("login"))


@app.route("/polls", methods=["POST", "GET"])
def polls():
  if request.method == "POST":
    selected_option = request.form['choice']
    user_id = session["user"]
    with open('voting_status.json', 'r') as file:
      voting_status = json.load(file)
    voting_status[user_id] = True
    with open('voting_status.json', 'w') as file:
      json.dump(voting_status, file)
    with open('poll_data.json', 'r') as file:
      poll_data = json.load(file)
    poll_data['responses'][selected_option] += 1
    with open('poll_data.json', 'w') as file:
      json.dump(poll_data, file)
    flash("Your vote was submitted")
    return redirect(url_for("polls"))
  else:
    if "user" in session:
      with open('poll_data.json', 'r') as file:
        poll_data = json.load(file)
      question = poll_data['question']
      responses = poll_data['responses']
      user = session["user"]
      options = options = list(responses.keys())
      counts = [int(count) for count in responses.values()]
      fig = go.Figure(data=go.Bar(x=options, y=counts))
      fig.update_layout(title='Poll Results: {}'.format(question),
                        xaxis_title='Options',
                        yaxis_title='Number of Responses')
      graph_div = fig.to_html(full_html=False)
      with open('voting_status.json', 'r') as file:
        voting_status = json.load(file)
      has_voted = user in voting_status
      return render_template('polls.html',
                             graph_div=graph_div,
                             has_voted=has_voted,
                             poll_data=poll_data)
    else:
      flash("You need to be logged in to use this!")
      return redirect(url_for("login"))


@app.route("/ee")
def rascam():
  print("rascam")
  return "e"


if __name__ == "__main__":
  print("nein")
  app.run(host='0.0.0.0', port=8080)
