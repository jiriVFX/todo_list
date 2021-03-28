from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired


# WTForm
class AddTaskForm(FlaskForm):
    task_name = StringField("Task name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    finish_by = DateTimeField("Finish by", validators=[DataRequired()])
    submit = SubmitField("Add Task")
