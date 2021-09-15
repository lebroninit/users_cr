from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/users/new')
def funny():
    return render_template("create.html")

@app.route('/users/<id>')
def user(id):
    user = User.get_user(id)
    return render_template("user.html" , this_user = user )

@app.route('/users/<id>/edit')
def edit(id):
    user = User.get_user(id)
    return render_template("edit.html", this_user = user)

@app.route('/delete', methods=["post"])
def delete():
    session["id"] = request.form["id"]
    User.delete(session["id"])
    return redirect("/users")

@app.route('/sendToUser', methods=["post"])
def sendToUser():
    session["id"] = request.form["id"]
    return redirect(f'/users/{session["id"]}')

@app.route('/sendToUsers', methods=["post"])
def sendToUsers():
    return redirect("/users")

@app.route('/sendToEdit', methods=["post"])
def sendToEdit():
    session["id"] = request.form["id"]
    return redirect(f'/users/{session["id"]}/edit')

@app.route("/update_user", methods=["post"])
def update_user():
    data = {
        "id": session["id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    return redirect("/users")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/sendToCreate", methods=["POST"])
def sendToCreate():
    return redirect("/users/new")

if __name__ == "__main__":
    app.run(debug=True)