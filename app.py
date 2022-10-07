# The main app of this flask todo app
# The code are adapted from the source code on https://www.python-engineer.com/posts/flask-todo-app/ by Python Engineer

# Import flask and SQLAlchemy library
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Create the flask with static folder name static in the same level of directory with the app.py
app = Flask(__name__, static_folder='./static')


# Configure the SQL database for the app
# Specify the location of the SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Don't track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Conifgure the SQL database with above specifications
db = SQLAlchemy(app)


# Model class for the Todo table
class Todo(db.Model):
    # Todo should have an ID as primary key for query
    id = db.Column(db.Integer, primary_key=True)
    # Todo should have a title which describe the actionable item inside
    title = db.Column(db.String(100))
    # Completeness status
    complete = db.Column(db.Boolean)


# API route for adding a new todo item
@app.route("/add", methods=["POST"])
def add():
    # Get the description of todo task from the user submitted form
    # and use it as the todo item's title in the database
    title = request.form.get("description")
    # Initially the todo item's  completeness should set to false (ongoing)
    new_todo = Todo(title=title, complete=False)
    # Add the new todo item to database
    db.session.add(new_todo)
    # Commit the change
    db.session.commit()
    # Redirect to the home page with updated todo list
    return redirect(url_for("home"))


# API route for updating the complete status of a todo 
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # Locate the todo that will be updated via its primary key "ID"
    # Get the first matching result
    todo = Todo.query.filter_by(id=todo_id).first()
    # Switch its completeness status
    todo.complete = not todo.complete
    # Commit the change
    db.session.commit()
    # Redirect to the home page with updated todo list
    return redirect(url_for("home"))


# API route for deleting a todo item
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Locate the todo that will be deleted via its primary key "ID"
    # Get the first matching result
    todo = Todo.query.filter_by(id=todo_id).first()
    # Remove the item from the database
    db.session.delete(todo)
    # Commit the change 
    db.session.commit()
    # Redirect to the home page with updated todo list
    return redirect(url_for("home"))


# API route for searching a todo item
@app.route("/search", methods=["POST"])
def search():
    # Get the searching keyword from the form submitted by users
    keyword = request.form.get("keyword")
    # If no keyword is given set the keyword to empty text
    if keyword is None:
        keyword = ""
    # Get all todo items stored in the database
    todo_list = Todo.query.all()
    # Accumulate the matching search results
    search_results = []
    # Iterate through the stored todo items
    for todo in todo_list:
        # Case-insensitive search the matching todo items
        if keyword.lower() in todo.title.lower():
            # Append found matched items to the list
            search_results.append(todo)
    
    # Redirect to the home page with updated todo list
    return render_template("base.html", todo_list=search_results)

# API route for directing to the main page
@app.route("/")
def home():
    # Get all stored todo items
    todo_list = Todo.query.all()
    # Display them in the main page
    return render_template("base.html", todo_list=todo_list)


# When run this file call the functions below
if __name__ == "__main__":
    # Within the context of this application
    with app.app_context():
        # Create the SQL database
        db.create_all()
    # Find the port defined in the environment (if not exist use default port 5000)
    port = int(os.environ.get('PORT', 5000))
    # Run the app on the local host with assigned port
    app.run(host='0.0.0.0', port=port)
