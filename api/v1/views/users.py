from flask import request, jsonify

from api.v1.models import User
from api.v1.views import app_views


@app_views.route("/users", strict_slashes=False, methods=["POST"])
def create():
    """Create a new user resource
    """
    json = request.get_json()
    print(json)
    user = User(**json)
    user.save()
    return jsonify({"user_id": user.id})


@app_views.route("/users/<id>", strict_slashes=False, methods=["GET"])
def get_user_byID(id):
    """Get a user by his ID
    """
    user = User.query.get_or_404(id)
    return jsonify(user.as_dict())
