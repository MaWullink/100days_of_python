from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

class MyForm(FlaskForm):
    edit_rating = FloatField(label="Edit rating")
    edit_review = StringField(label="Edit review", validators=[Length(max=250)])
    edit_rank = IntegerField(label="Edit rank")
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    movie_title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField("Add")