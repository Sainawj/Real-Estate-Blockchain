from flask import Blueprint, request, jsonify
from app.services.contract_service import deploy_contract, interact_contract

bp = Blueprint('contract', __name__, url_prefix='/contract')

@bp.route('/deploy', methods=['POST'])
def deploy_contract_route():
    address = deploy_contract()
    return jsonify(contract_address=address)

@bp.route('/interact', methods=['POST'])
def interact_contract_route():
    data = request.json
    result = interact_contract(data)
    return jsonify(result)