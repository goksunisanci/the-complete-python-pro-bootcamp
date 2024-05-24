from flask import Flask, render_template, jsonify, request
from sqlalchemy.sql.expression import func
from distutils.util import strtobool

from random import choice

from .models import db, Cafe
from .data.cafes import cafes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # execute once for adding datas to database.
    # for cafe in cafes:
    #     new_cafe = Cafe(
    #         id=cafe["id"],
    #         name=cafe["name"],
    #         map_url=cafe["map_url"],
    #         img_url=cafe["img_url"],
    #         location=cafe["location"],
    #         has_socket=cafe["has_socket"],
    #         has_toilet=cafe["has_toilet"],
    #         has_wifi=cafe["has_wifi"],
    #         can_take_calls=cafe["can_take_calls"],
    #         seats=cafe["seats"],
    #         coffee_price=cafe["coffee_price"]
    #     )
    #     db.session.add(new_cafe)
    #     db.session.commit()
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    result = (db.session.execute(db.select(Cafe).order_by(func.random())))
    random_cafe = result.scalars().first()
    cafe_info = jsonify(Cafe=random_cafe.to_dict())
    return cafe_info


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    cafes_info = jsonify(Cafes=[cafe.to_dict() for cafe in all_cafes])
    return cafes_info


@app.route("/search")
def search_cafe_for_location():
    query_location = request.args.get("location")
    cafes_in_location = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
    print(cafes_in_location)
    if cafes_in_location:
        cafe = jsonify(Cafe=[cafe.to_dict() for cafe in cafes_in_location])
        return cafe
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_socket=strtobool(request.form.get("has_socket")),
        has_toilet=strtobool(request.form.get("has_toilet")),
        has_wifi=strtobool(request.form.get("has_wifi")),
        can_take_calls=strtobool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_with_id = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe_with_id:
        cafe_with_id.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe_with_id = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe_with_id:
            db.session.delete(cafe_with_id)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted."})
        else:
            return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})
