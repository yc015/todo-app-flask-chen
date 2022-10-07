Yida Chen  

# Flask TODO App
An instance of this todo app is hosted on [https://todo-app-flask-chen.herokuapp.com/](https://todo-app-flask-chen.herokuapp.com/).

# Content
./app.py: The main python file for launching the flask application
templates/base.html: The view of the todo app.
./static/style/style.css: The CSS styling of the widgets inside the todo app

# How to interact with the todo app
1. Go to the app page: [https://todo-app-flask-chen.herokuapp.com/](https://todo-app-flask-chen.herokuapp.com/)  
2. The center emerald green panel shows your todo items stored in the database.
3. To add a new todo item in the list, enter the description of your task at the top input box and click `Add` once finished.
4. New todo item will be displayed in the panel below.
5. To switch a todo item's completeness status, click the blue `Update` button on the right of the item.
6. To remove a todo item, click the red `Delete` button on the right.
7. To search todo items, type in your searching keywords at the bottom input box and click `Search` button.
8. To reset the search results (back to the original list of all todo items), click the `Reset` button.

If you want to build this app from source:
9. Install Python >= 3.7
10. pip install requirements.txt
11. Launch the app by `$ python app.py`
12. Go to the page `http://localhost:5000/` in your browser.

# References
The creation of this app using the source code from [Python Engineer](https://www.python-engineer.com/)'s tutorial "Python Flask Beginner Tutorial - Todo App," [https://www.python-engineer.com/posts/flask-todo-app/](https://www.python-engineer.com/posts/flask-todo-app/). Additional references to the source code can be found in the comment at the **top** of each file.
