from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)

Bootstrap5(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label="Location of the cafe (use URL form Google Maps)", validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening time e.g 9 AM", validators=[DataRequired()])
    closing_time = StringField(label="Opening time e.g 5:30 PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee rating", validators=[DataRequired()],
                                choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField(label="Wifi rating", validators=[DataRequired()],
                                choices=["🛜️", "🛜️🛜️", "🛜️🛜️🛜️", "🛜️🛜️🛜️🛜️️", "🛜️🛜️🛜️🛜️🛜️"])
    power_outlet_rating = SelectField(label="Power rating", validators=[DataRequired()],
                              choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()

    fieldnames = ["Cafe Name", "Location", "Open", "Close", "Coffee", "Wifi", "Power"]

    if form.validate_on_submit():

        file_exists = os.path.exists("cafe-data.csv")

        with open("cafe-data.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "Cafe Name": form.cafe.data,
                "Location": form.location.data,
                "Open": form.open_time.data,
                "Close": form.closing_time.data,
                "Coffee": form.coffee_rating.data,
                "Wifi": form.wifi_rating.data,
                "Power": form.power_outlet_rating.data,
            })

        return redirect(url_for("cafes"))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    if os.path.exists("cafe-data.csv"):
        with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file)
            list_of_rows = list(csv_data)
            return render_template("cafes.html", cafes=list_of_rows)
    else:
        return render_template("cafes.html")




if __name__ == '__main__':
    app.run(debug=True)

