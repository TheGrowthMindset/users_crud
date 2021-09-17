from flask import render_template, redirect, session, request

from flask_app import app
# ...server.py


from user import User
# import the class from user.py

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    for user in users:
        print(user)
    return render_template("read(all).html", users = users)


@app.route("/user_signup")
def sign_up_page():
    return render_template('create.html')

@app.route("/create_new", methods=['POST'])
def add_new_user():
    data = { 
    # this 'email' Key in data must be named to match the placeholder in the query.
    "fname": request.form["fname"],
    "lname": request.form["lname"],
    'mail' : request.form['mail'] 
}
    User.create_new(data)
    return redirect("/")



@app.route("/<int:id>")
def user(id):
    data = {
        "id" : id
    }
    user = User.one_user(data)
    return render_template("show.html", user = user)

@app.route("/users/<int:id>/edit/")
def edit(id):
    data = {
        "id" : id
    }

    user = User.one_user(data)
    return render_template("edit.html", edituser = user)

@app.route("/edituser/<int:id>", methods=['GET','POST'])
def edituser(id):
    print(id)
    data = {
        "id" : id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    
    User.edit(data)
    print(data)
    return redirect("/users/" + str(id))

@app.route("/users/<int:id>/delete/")
def delete(id):
    data = {
        "id" : id
    }

    user = User.delete(data)
    return redirect("/users")
