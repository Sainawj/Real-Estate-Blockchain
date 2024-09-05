from flask import Blueprint, jsonify, request
from app.models import User, Transaction, Property
from bson import ObjectId

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/api/user/<user_id>', methods=['GET'])
def get_user_info(user_id):
    user = User.objects.get_or_404(id=ObjectId(user_id))
    user_data = {
        'full_name': user.full_name,
        'location': user.location,
        'email': user.email,
        'phone': user.phone,
        'properties_owned': len(user.properties_owned),
        'properties_leased': len(user.properties_leased)
    }
    return jsonify(user_data)

@dashboard_bp.route('/api/transactions/<user_id>', methods=['GET'])
def get_transaction_history(user_id):
    transactions = Transaction.objects(user_id=ObjectId(user_id))
    transactions_data = [{
        'date': transaction.date,
        'amount': transaction.amount,
        'description': transaction.description,
        'check': transaction.check,
        'who': transaction.who,
        'balance': transaction.balance,
        'receipt': transaction.receipt,
        'balance_paid': transaction.balance_paid,
        'interest': transaction.interest,
        'fees': transaction.fees
    } for transaction in transactions]
    return jsonify(transactions_data)

@dashboard_bp.route('/api/watchlist/<user_id>', methods=['GET'])
def get_watchlist(user_id):
    user = User.objects.get_or_404(id=ObjectId(user_id))
    watchlist_data = [{
        'property_id': property.id,
        'image': property.image_url
    } for property in user.watchlist]
    return jsonify(watchlist_data)