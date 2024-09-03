import ipfshttpclient

client = ipfshttpclient.connect()

def add_file(file_path):
    res = client.add(file_path)
    return res['Hash']

def get_file(ipfs_hash):
    return client.cat(ipfs_hash)