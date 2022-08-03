from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import func

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# Take a list of cafe objects, and returns a list of dict of theses cafe objects
def to_dict(list_of_Cafe_obj):
    cafes_list = []
    for cafe in list_of_Cafe_obj:
        new_cafe = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafes_list.append(new_cafe)
    return cafes_list

## Routes
@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafe = Cafe.query.order_by(func.random()).first()
    # all_cafes = db.session.query(Cafe).all()
    # cafe = all_cafes[random.randint(1, 21)]
    print(cafe.name)

    return render_template("index.html")

@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    # print(len(cafes))
    cafes_list = to_dict(cafes)

    cafes_json = jsonify(cafes_list)
    print(cafes_json)

    return render_template("index.html")


@app.route("/search")
def search_cafe_by_location():
    query_location = request.args.get("location")
    corresponding_cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    # print(len(corresponding_cafes))
    if len(corresponding_cafes) == 0:
        cafes_json = jsonify(to_dict(corresponding_cafes))
        # print(cafes_json)
        return cafes_json
    else:
        error = jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        # print(error)

    return render_template("index.html")

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe is not None:
        new_price = request.args.get("new_price")
        print(new_price)
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(response={"success": f"Successfully updated the coffee price for the cafe {cafe.name}."})
    else:
        return jsonify(error={"Not Found": "Sorry, no cafe with that id was found in the database."}), 404


## HTTP DELETE - Delete Record
DELETE_API_KEY = "TopSecretAPIKey"

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != DELETE_API_KEY:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api key."}), 403
    else:
        cafe = Cafe.query.get(cafe_id)
        if cafe is not None:
            db.session.delete(cafe)
            db.session.commit()

            return jsonify(response={"Success": f"The cafe {cafe.name} was successfully deleted from the database."})

        else:
            return jsonify(error={"Not Found": "Sorry, no cafe with that id was found in the database."}), 404

if __name__ == '__main__':
    app.run(debug=True)