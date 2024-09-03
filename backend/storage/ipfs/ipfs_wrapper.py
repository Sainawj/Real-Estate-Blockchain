import subprocess
import json

def add_file_to_ipfs(filename, file_content):
    try:
        # Call the Node.js script to add the file
        result = subprocess.run(
            ['node', 'backend/storage/ipfs/add_file.js', filename, file_content],
            capture_output=True, text=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error adding file to IPFS: {e}")
        return None

def get_file_from_ipfs(ipfs_hash):
    try:
        # Call the Node.js script to get the file
        result = subprocess.run(
            ['node', 'backend/storage/ipfs/get_file.js', ipfs_hash],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        print(f"Error retrieving file from IPFS: {e}")
        return None