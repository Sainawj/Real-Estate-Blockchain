from storage.ipfs.ipfs_utils import addFile, getFile

def test_upload_to_ipfs():
    file_content = "Sample file content"
    result = addFile({'path': 'sample.txt', 'content': file_content.encode('utf-8')})
    assert 'path' in result

def test_retrieve_from_ipfs():
    file_content = "Sample file content"
    result = addFile({'path': 'sample.txt', 'content': file_content.encode('utf-8')})
    retrieved_content = getFile(result['path'])
    assert retrieved_content.decode('utf-8') == file_content