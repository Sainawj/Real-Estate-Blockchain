from mongodb_config import insert_document

# Example property document
property_document = {
    'title': 'Beautiful House',
    'description': 'A beautiful house in the countryside',
    'price': 100.5,
    'owner': '0xOwnerAddress',
    'ipfs_hash': 'Qm...'  # Link to IPFS file
}

# Insert the document
document_id = insert_document(property_document)
print(f'Document inserted with ID: {document_id}')