from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from forms import AddTaskForm

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# .env file should contain your API_KEY, e.g. API_KEY=YourOwnApiKey
API_KEY = os.environ.get("API_KEY")
# Connect to the Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# To-do list Table Configuration
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=True)
    finish_by = db.Column(db.DateTime(timezone=True), nullable=True)
    finished = db.Column(db.Boolean, nullable=False)


@app.route("/")
def home():
    new_form = AddTaskForm()
    page = request.args.get("page", default=1, type=int)
    todo = db.session.query(ToDo).paginate(per_page=10)
    # user_agent = request.headers.get("User-Agent")
    return render_template("todo.html", tasks=todo, form=new_form)


@app.route("/add", methods=["POST"])
def add():
    new_list = ToDo(
        task_name=request.form["task_name"],
        description=request.form["description"],
        finish_by=request.fomr["finish_by"],
        finished=False,
    )
    db.session.add(new_list)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/edit")
def edit():
    page = request.args.get("page", default=1, type=int)
    return render_template("todo.html")


@app.route("/remove")
def remove():
    page = request.args.get("page", default=1, type=int)
    return render_template("todo.html")


if __name__ == '__main__':
    # db.create_all()

    # todo_list = ToDo(task_name="Third record", description="Finish the third record", finish_by=datetime.now(), finished=False)
    # db.session.add(todo_list)
    # db.session.commit()

    app.run(debug=True)
