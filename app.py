"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "flyersareawesome"

connect_db(app)


# *****************************
# RESTFUL CUPCAKES JSON API
# *****************************
@app.route("/api/cupcakes")
def get_all_cupcakes():
    """Return all cupcakes in db as JSON.

    Returns JSON like:
        {cupcakes: [{id, flavor, rating, size, image}, ...]}
    """

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Returns JSON for a specific cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add a new cupcake and returns JSON.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        rating=request.json["rating"],
        size=request.json["size"],
        image=request.json["image"] or None
    )

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)
