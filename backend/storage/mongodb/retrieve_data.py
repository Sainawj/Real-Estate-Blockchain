from mongodb_config import get_documents

# Example query
query = {'owner': '0xOwnerAddress'}

# Retrieve the documents
documents = get_documents(query)
for doc in documents:
    print(doc)