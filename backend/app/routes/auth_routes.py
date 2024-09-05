from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = register_user(data)
    return jsonify(user), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = login_user(data)
    return jsonify(token=token)