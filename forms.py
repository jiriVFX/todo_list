from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


# WTForm
class AddTaskForm(FlaskForm):
    task_name = StringField("Task name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    finish_date = DateField("Finish date", format="%d-%m-%Y", validators=[DataRequired()])
    finish_time = TimeField("Finish time", format="%H:%M", validators=[DataRequired()])
    submit = SubmitField("Add Task")
