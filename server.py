from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)



# relevant code snippet from server.py
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect("/users")

@app.route('/users/new')
def funny():
    return render_template("create.html")

@app.route("/sendTo", methods=["POST"])
def sendTo():
    return redirect("/users/new")

if __name__ == "__main__":
    app.run(debug=True)