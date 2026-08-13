from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Please enter your email."),
            Email(message="Please enter a valid email address.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Please enter your password."),
            Length(min=8, message="Password must be at least 8 characters.")
        ]
    )
    submit = SubmitField("Submit")