const { getFile } = require('./ipfs_utils');

const ipfsHash = process.argv[2];

getFile(ipfsHash)
    .then(file => {
        console.log(file.toString());
    })
    .catch(error => {
        console.error('Error:', error);
    });