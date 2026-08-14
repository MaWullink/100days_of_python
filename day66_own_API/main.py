from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        cafes_dict = {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }
        return cafes_dict


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    cafe_dict = Cafe.to_dict(random_cafe)
    return jsonify(cafe_dict)

@app.route("/all")
def get_all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes_dict = [Cafe.to_dict(cafe) for cafe in all_cafes]
    return jsonify(cafes_dict)

@app.route("/search")
def search():
    location = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location) ).scalars().all()
    if all_cafes:
        cafes_dict = [Cafe.to_dict(cafe) for cafe in all_cafes]
        return jsonify(cafes_dict)
    else:
        return jsonify(error="Cafe not found"), 404

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def patch_new_price(id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get(Cafe, id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
