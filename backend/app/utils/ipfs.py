import ipfshttpclient

class IPFS:
    def __init__(self):
        self.client = ipfshttpclient.connect()

    def add_file(self, file_path):
        res = self.client.add(file_path)
        return res['Hash']

    def get_file(self, file_hash):
        return self.client.cat(file_hash)