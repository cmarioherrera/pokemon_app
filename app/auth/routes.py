import logging
from flask import request, jsonify
from . import auth_blueprint
from flask_jwt_extended import create_access_token


from app.auth.services import AuthServices


@auth_blueprint.route("/login", methods=['POST'])
def login():
    """
    User authenticate method.
    ---
    description: Authenticate user with supplied credentials.
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    responses:
      200:
        description: User successfully logged in.
      400:
        description: User login failed.
    """
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        user = AuthServices.authenticate(username, password)
        if not user:
            raise Exception("User not found!")

        access_token = create_access_token(identity=user.username)
        resp = jsonify({"message": "User authenticated", "jwt-token": f"Bearer {access_token}"})
        resp.status_code = 200

    except Exception as e:
        logging.error(e, exc_info=True)
        resp = jsonify({"message": "Bad username and - or password"})
        resp.status_code = 401

    return resp
