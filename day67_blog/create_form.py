from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField

class AddPost(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(250)])
    subtitle = StringField(label="Subtitle", validators=[DataRequired(), Length(250)])
    author = StringField(label="Author", validators=[DataRequired(), Length(250)])
    img_url = StringField(label="Image URL", validators=[DataRequired(), URL(), Length(250)])
    body = CKEditorField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit post")

class EditPost(FlaskForm):
    title = StringField(label="Title")
    subtitle = StringField(label="Subtitle")
    author = StringField(label="Author")
    img_url = StringField(label="Image URL")
    body = CKEditorField(label="Content")
    submit = SubmitField(label="Edit post")