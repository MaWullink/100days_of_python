import os

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from create_form import AddMovie, MyForm



load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"

Bootstrap5(app)


# DATABASE
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# MOVIE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250))
    url: Mapped[str] = mapped_column(String(500), nullable=False)


with app.app_context():
    db.create_all()


# TMDB
API_KEY = os.getenv("MOVIE_API_KEY")

SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
MOVIE_ENDPOINT = "https://api.themoviedb.org/3/movie"


# HOME
@app.route("/")
def home():
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.ranking)
    ).scalars().all()

    return render_template("index.html", movies=movies)


# UPDATE MOVIE
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = MyForm()
    movie = db.session.get(Movie, id)

    if form.validate_on_submit():

        if form.edit_rating.data:
            movie.rating = form.edit_rating.data

        if form.edit_review.data:
            movie.review = form.edit_review.data

        if form.edit_rank.data:
            movie.ranking = form.edit_rank.data

        db.session.commit()

        return redirect(url_for("home"))

    return render_template(
        "edit.html",
        movie=movie,
        form=form
    )


# DELETE MOVIE
@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.get(Movie, id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


# SEARCH FOR MOVIE
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()

    if form.validate_on_submit():

        title = form.movie_title.data

        params = {
            "api_key": API_KEY,
            "query": title
        }

        response = requests.get(
            SEARCH_ENDPOINT,
            params=params
        )

        movies = response.json()["results"]

        return render_template(
            "select.html",
            options=movies
        )

    return render_template(
        "add.html",
        form=form
    )


# SELECT MOVIE
@app.route("/select/<int:id>")
def select(id):

    params = {
        "api_key": API_KEY
    }

    response = requests.get(
        f"{MOVIE_ENDPOINT}/{id}",
        params=params
    )

    movie = response.json()

    new_movie = Movie(
        title=movie["title"],
        year=int(movie["release_date"][:4]),
        description=movie["overview"],
        rating=0,
        ranking=0,
        review="",
        url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("update", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)