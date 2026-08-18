import os.path

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.session.commit()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        password = request.form.get("password")

        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(password, method="scrypt"),
            name=request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("login.html")
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = db.session.execute(
            db.select(User).where(User.email == request.form.get("email"))
        ).scalar()

        if user is None:
            flash("User not found")
            return render_template("login.html")

        if check_password_hash(user.password, request.form.get("password")):
            return render_template("secrets.html", user=user)

        flash("Password incorrect")
        return render_template("login.html")

    return render_template("login.html")



@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    directory = os.path.join(app.root_path, "static", "files")
    return send_from_directory(directory=directory, path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
