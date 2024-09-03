from flask import Flask, request, jsonify
from backend.models import PropertyModel
from storage.ipfs.ipfs_utils import addFile
from storage.ipfs.ipfs_wrapper import add_file_to_ipfs

app = Flask(__name__)

@app.route('/add_property', methods=['POST'])
def add_property():
    try:
        property_data = request.json
        if 'filename' not in property_data or 'file_content' not in property_data:
            return jsonify({"error": "Missing filename or file_content"}), 400
        
        # Save file to IPFS
        ipfs_result = addFile({
            'path': property_data['filename'],
            'content': property_data['file_content'].encode('utf-8')
        })
        
        property_data['ipfs_hash'] = ipfs_result['Hash']  # Ensure 'Hash' key exists in IPFS result
        
        # Save metadata to MongoDB
        property_id = PropertyModel.insert_property(property_data)
        return jsonify({"property_id": str(property_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_properties/<owner>', methods=['GET'])
def get_properties(owner):
    try:
        properties = PropertyModel.get_properties_by_owner(owner)
        if not properties:
            return jsonify({"error": "No properties found for this owner"}), 404
        return jsonify(properties)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)