from flask import Blueprint, request, jsonify
from app.services.property_service import list_property, get_properties, purchase_property

bp = Blueprint('property', __name__, url_prefix='/property')

@bp.route('/', methods=['POST'])
def list_property_route():
    data = request.json
    property = list_property(data)
    return jsonify(property), 201

@bp.route('/', methods=['GET'])
def get_properties_route():
    properties = get_properties()
    return jsonify(properties)

@bp.route('/<int:id>/purchase', methods=['POST'])
def purchase_property_route(id):
    data = request.json
    transaction = purchase_property(id, data)
    return jsonify(transaction)